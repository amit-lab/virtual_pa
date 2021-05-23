import requests
import user_data
from sms_sender import SendSms


class WeatherData:
    def __init__(self):
        self.api_key = user_data.open_weather_api_key
        self.current_data_url = "https://api.openweathermap.org/data/2.5/weather"
        self.one_call_url = "https://api.openweathermap.org/data/2.5/onecall"
        self.status = self.check_names()
        if self.status:
            self.names = self.get_names()
            self.city_name = self.names[0]
            self.country_name = self.names[1]
            long_lat = self.get_current_data()
            self.MY_LAT = long_lat['lat']
            self.MY_LON = long_lat['lon']
            self.weather_data = self.get_data()


    def get_data(self):
        parameters = {
            "lat": self.MY_LAT,
            "lon": self.MY_LON,
            "appid": self.api_key,
            "units": "metric",
            "exclude": "current,minutely,daily,alerts"
        }
        response = requests.get(self.one_call_url, params=parameters)
        response.raise_for_status()
        weather_data = response.json()['hourly']
        return weather_data

    def get_current_data(self):
        parameters = {
                "q": f"{self.city_name},{self.country_name}",
                "appid": self.api_key,
                "units": "metric"
                }
        response = requests.get(self.current_data_url, params=parameters)
        response.raise_for_status()
        weather_data = response.json()
        data = {
                'status': weather_data['weather'][0]['description'],
                'temp': weather_data['main']['temp'],
                'wind speed': weather_data['wind'],
                'lon': weather_data['coord']['lon'],
                'lat': weather_data['coord']['lon'],
        }

        return data


    def rain_alert(self):
        will_rain = False
        for hour in range(7):
            for current in self.weather_data[hour]['weather']:
                # print(current['id'])
                if current['id'] < 700:
                    will_rain = True

        if will_rain:
            SendSms("Today there is probability of rain fall.\n\
                    So Bring an Umbrella with you if you are going outside")
        return will_rain

    def save_names(self, city_name, country_name):
        with open('data/weather.txt', 'w') as f:
            f.write(city_name+'\n'+country_name)

    def check_names(self):
        try:
            with open('data/weather.txt', 'r') as _:
                return True
        except FileNotFoundError:
            return False

    def get_names(self):
        if self.status:
            with open('data/weather.txt', 'r') as f:
                return f.readlines()


