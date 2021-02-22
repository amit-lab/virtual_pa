import requests
import lxml
from bs4 import BeautifulSoup

class PriceTracker:
    def __init__(self, url):
        print(self.check_process(1000))
        self.save_url()

    def check_process(self, prefered_price):
        responce = requests.get("https://www.flipkart.com/samsung-23-8-inch-curved-full-hd-led-backlit-va-panel-monitor-lc24f390fhwxxl/p/itmezu53yhwg2ayg?pid=MONEZU4Z8BYBV2GZ&lid=LSTMONEZU4Z8BYBV2GZCQOCQM&marketplace=FLIPKART&srno=b_1_1&otracker=hp_reco_Discounts%2Bfor%2BYou_1_16.dealCard.OMU_cid%3AS_F_N_6bo_g0i_9no__d_20-100__NONE_ALL%3Bnid%3A6bo_g0i_9no_%3Bet%3AS%3Beid%3A6bo_g0i_9no_%3Bmp%3AF%3Bct%3Ad%3B_10&otracker1=hp_reco_WHITELISTED_personalisedRecommendation%2Fdiscount_Discounts%2Bfor%2BYou_DESKTOP_HORIZONTAL_dealCard_cc_1_NA_view-all_10&fm=personalisedRecommendation%2Fdiscount&iid=260aadc1-2b33-4f1f-bd39-1bbc8acb0fca.MONEZU4Z8BYBV2GZ.SEARCH&ppt=browse&ppn=browse&ssid=4inhviylt8tdg5c01613382765652", 'lxml')
       soup = BeautifulSoup(responce.text, 'lxml')
       price = soup.find(class_="_30jeq3 _16Jk6d").string
       current_price = ''
       for txt in list(price):
           if txt in [str(i) for i in range(10)]:
               current_price += txt
       print(current_price[1:])
       if int(prefered_price) > int(current_price[1:]):
           return True
       return False

   def save_url(self):
       with open('url.txt', 'w') as f:
           f.write(url)



# For testing
track = PriceTracker()


