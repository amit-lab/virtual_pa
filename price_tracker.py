import requests
import lxml
from bs4 import BeautifulSoup
from sms_sender import SendSms

class PriceTracker:
    def __init__(self):
        self.status = self.get_url()

    def check_price(self):
        responce = requests.get(self.status[0], 'lxml')
        soup = BeautifulSoup(responce.text, 'lxml')
        product_name = soup.find(class_='B_NuCI').text
        price = soup.find(class_="_30jeq3 _16Jk6d").text
        price = price.replace(',', '')
        current_price = ''
        is_low = ''

        if not price.isnumeric():
            price = price[1:]

        for txt in list(price):
            if txt in [str(i) for i in range(10)]:
                current_price += txt
        if int(self.status[1]) <= int(current_price):
            is_low = 'no'
        else:
            is_low = 'yes'

        data = {'product name':product_name[:35]+'...',
                'current price':current_price,
                'desired price':self.status[1],
                'price low':is_low}
        if is_low == 'yes':
            self.send_sms(data)
        return data

    def get_url(self):
        try:
            with open('data/url.txt', 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            return False

    def save_url(self, url, price):
        with open('data/url.txt', 'w') as f:
            f.write(url+'\n'+str(price))

    def send_sms(self, data):
        text = f"""\nProduct name: {data['product name']}\nCurrent price: {data['current price']}\ntoday you will save some money. So go buy it."""
        SendSms(text)
        


