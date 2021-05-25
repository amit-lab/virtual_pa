import os
import wikipedia
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
            result = wikipedia.summery(text, sentences=2)
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
        if "the time" in text:
            cur_time = datetime.datetime.now().strftime("%H:%M:%S")
            vr.speak(f"sir, current time is {cur_time}")
        if "weather" in text:
            weather = WeatherData()
            cur_weather = weather.get_current_data()
            vr.speak(f"current weather is {cur_weather['status']}, \
                    having {cur_weather['temp']} temperature")
        if "current price" in text:
            tracker = PriceTracker()
            if "amazon" in text:
                amazon_price = tracker.price_on_amazon()
                vr.speak(f"currently, price of your selected product on amazon is {amazon_price}")
            if "flipkart" in text:
                flipkart_price = tracker.price_on_flipkart()
                vr.speak(f"currently, price of your selected product on flipkart is {flipkart_price}")
            



