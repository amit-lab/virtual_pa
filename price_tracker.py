import requests
import lxml
from bs4 import BeautifulSoup
from sms_sender import SendSms


class PriceTracker:
    def __init__(self):
        self.status = self.check_url()
        if self.status:
            self.url_data = self.get_url()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
            'Accept-Language': 'en-US,en;q=0.5',
        }

    def get_data(self):
        """
           This function will get the current prices from all three websites
           simultaneously
        """
        # Fetching data
        fdata = self.price_on_flipkart()
        adata = self.price_on_amazon()
        #sdata = self.price_on_snapdeal()
        # Analysing data
        if adata[1] > fdata[1]:
            cheaper = 'flipkart'
        elif adata[1] < fdata[1]:
            cheaper = 'amazon'
        else:
            cheaper = 'both'

        is_low = 'yes'
        if adata[1] > int(self.url_data[2]) or fdata[1] > int(self.url_data[2]):
            is_low = 'no'

        data = {
            'amazon': adata,
            'flipkart': fdata,
        #    'snapdeal': sdata,
            'low price website': cheaper,
            'desired price': self.url_data[2],
            'is low': is_low,
        }
        return data

    def check_price(self):
        is_low = ''
        
        if int(self.data[1]) <= int(current_price):
            is_low = 'no'
        else:
            is_low = 'yes'

        data = {'product name':product_name[:35]+'...',
                'current price':current_price,
                'desired price':self.data[1],
                'price low':is_low}
        if is_low == 'yes':
            self.send_sms(data)
        return data

    def price_on_flipkart(self):
        """This function will get the current price of product from flipkart"""
        #Getting html page data from flipkart url
        responce = requests.get(self.url_data[0], headers=self.headers)
        soup = BeautifulSoup(responce.text, 'lxml')
        #Filtering the data
        product_name = soup.find(class_='B_NuCI').text
        price = soup.find(class_="_30jeq3 _16Jk6d").text
        #Purifying filtered data and comverting into desired format
        price = price.replace(',', '')
        current_price = ''
        if not price.isnumeric():
            price = price[1:]
        for txt in list(price):
            if txt in [str(i) for i in range(10)]:
                current_price += txt
    
        data = [f"{product_name[:35]}...", int(current_price)]
        return data

    def price_on_amazon(self):
        """This function will get the current price of product from amazon"""
        #Getting html page data from amazon url
        res = requests.get(self.url_data[1], headers=self.headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')
        #Filtering the data
        price = soup.find("span", {"id": "priceblock_dealprice"})
        if price == None:
            price = soup.find("span", {"id": "priceblock_ourprice"})
        product_name = soup.find("span", 
                                 {"id": "productTitle"}).text.replace('\n', '')
        #Purifying filtered data and converting into desired format
        price = price.text
        price = price.split('.')[0]
        price = price.replace(',', '')
        current_price = ''
        if not price.isnumeric():
            price = price[1:]
        for txt in list(price):
            if txt in [str(i) for i in range(10)]:
                current_price += txt
            
        data = [f"{product_name[:35]}...", int(current_price)]
        return data

    def price_on_snapdeal(self):
        """This function will get the current price of product from snapdeal"""
        
        res = requests.get(self.url_data[2], headers=self.headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')
        
        price = soup.find("span", {"class": "payBlkBig", "itemprop": "price"})
        product_name = soup.find("h1", {"class": "pdp-e-i-head", "itemprop": "name"})
        product_name = product_name.text.replace('\n', '')
        data = [f"{product_name[6:0]}", int(price.text)]
        return data

    def get_url(self):
        with open('data/url.txt', 'r') as f:
            return f.readlines()

    def check_url(self):
        """This function will check weather url already exists or not"""
        try:
            with open('data/url.txt', 'r') as f:
                return True
        except FileNotFoundError:
            return False

    def save_url(self, data):
        with open('data/url.txt', 'w') as f:
            f.write(data[0]+'\n'+data[1]+'\n'+data[2])

    def send_sms(self, data):
        text = f"""\nProduct name: {data['product name']}\nCurrent price: {data['current price']}\ntoday you will save some money. So go buy it."""
        SendSms(text)
        


