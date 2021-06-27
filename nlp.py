import os
import wikipedia as wiki
import webbrowser
from random import choice
import subprocess
import datetime
from weather_data import WeatherData
from price_tracker import PriceTracker


class Nlp:

    def gui_launcher(self, text, gui):
        text = text.lower()
        if "weather forcast" in text or "weather info" in text:
            gui.weather_page()
        if "price tracker" in text:
            gui.price_track_page()
        if "system" in text:
            gui.system_admin_page()

    def other_launcher(self, text):
        text = text.lower()
        if "firefox" in text or "browser" in text:
            os.system("firefox &")
        if "image editor" in text:
            os.system("gimp &")
        if "open browser" in text or "open google" in text:
            webbrowser.open(url="google.com", new=1)
        if "open youtube" in text:
            webbrowser.open(url="youtube.com", new= 1)
        if "video editor" in text:
            os.system("kdenlive &")

    def query(self, text):
        from voice_recognition import VoiceRecognition
        text = text.lower()
        vr = VoiceRecognition()
        if "search " in text:
            print(text[8:])
        if "wikipedia" in text:
            text = text.replace("wikipedia", "")
            result = wiki.summery(text, sentences=2)
            vr.speak(f"According to wikipedia, {result}")
        if "play music" in text:
            songs = subprocess.Popen("ls ~/Music/*.mp3", 
                    shell=True, 
                    stdout=subprocess.PIPE
            )
            all_songs = []
            for song in songs.stdout:
                song = str(song)
                all_songs.append(f"{song[1:-3]}'")
                
            os.system(f"open {choice(all_songs)}")
        if "system" in text:
            os.system("alacritty -e htop")
        if "the time" in text:
            cur_time = datetime.datetime.now().strftime("%H:%M:%S")
            vr.speak(f"sir, current time is {cur_time}")
            print(f"sir, current time is {cur_time}")
        if "weather" in text:
            weather = WeatherData()
            cur_weather = weather.get_current_data()
            vr.speak(f"current weather is {cur_weather['status']}, \
                    having {cur_weather['temp']} temperature")
            print(f"current weather is {cur_weather['status']}, having {cur_weather['temp']} temperature")
        if "current price" in text:
            tracker = PriceTracker()
            try:
                data = tracker.get_data()
            except Exception as e:
                vr.speak("Sir, you have not given url of the product you are trying to track. Please go to gui section and click on price tracker button and set urls first")
                print("Sir, you have not given url of the product you are trying to track. Please go to gui section and click on price tracker button and set urls first")

            if "amazon" in text:
                amazon_price = data['amazon']
                vr.speak(f"currently, price of your selected product {amazon_price[0]} on amazon is {amazon_price[1]}")
                print(f"currently, price of your selected product {amazon_price[0]} on amazon is {amazon_price[1]}")
            elif "flipkart" in text:
                flipkart_price = data['flipkart']
                vr.speak(f"currently, price of your selected product {flipkart_price[0]} on flipkart is {flipkart_price[1]}")
                print(f"currently, price of your selected product {flipkart_price[0]} on flipkart is {flipkart_price[1]}")
            else:
                vr.speak(f"Ok sir")
                vr.speak(f"Your product : {data['amazon'][0]} on amazon has price of rupees {data['amazon'][1]}")
                vr.speak(f"and {data['flipkart'][0]} on flipkart has price of rupees {data['flipkart'][1]}")
                vr.speak(f"currently price is low on {data['low price website']} which is {data[data['low price website']][1]}")
                vr.speak(f"and your desired price is {data['desired price']}")
                print(f"Your product : {data['amazon'][0]} on amazon has price of rupees {data['amazon'][1]}")
                print(f"and {data['flipkart'][0]} on flipkart has price of rupees {data['flipkart'][1]}")
                print(f"currently price is low on {data['low price website']} which is {data[data['low price website']][1]}")
                print(f"and your desired price is {data['desired price']}")

