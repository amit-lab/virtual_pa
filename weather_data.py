import requests
import user_data


class WeatherData:
    def __init__(self):
        self.api_key = user_data.open_weather_api_key
        self.OWM_Endpoint = user_data.open_weather_url
        self.MY_LAT = 19.751480
        self.MY_LON = 75.713890
        self.parameters = {
            "lat": self.MY_LAT,
            "lon": self.MY_LON,
            "appid": self.api_key,
            "units": "metric",
            "exclude": "current,minutely,daily,alerts"
        }
        self.weather_data = self.get_data()
        self.will_rain = self.rain_alert()

    def get_data(self):
        response = requests.get(self.OWM_Endpoint, params=self.parameters)
        response.raise_for_status()
        weather_data = response.json()['hourly']
        return weather_data

    def rain_alert(self):
        will_rain = False
        for hour in range(12):
            for current in self.weather_data[hour]['weather']:
                # print(current['id'])
                if current['id'] < 700:
                    will_rain = True

        # if will_rain:
        #     print("Bring an umbrella")
            # We can send the sms on our mobile using twilio api
        return will_rain


