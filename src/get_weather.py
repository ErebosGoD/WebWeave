import requests
from weathericondict import weather_icons
import os


class WeatherForecast():
    def __init__(self) -> None:
        self.file_path = os.path.join('flaskapp\src\static', 'weathermap.png')

        self.layer = ''

    def get_weather_forecast(self, location, api_key):
        location_response = requests.get(
            f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit={1}&appid={api_key}")
        data = location_response.json()
        latitude = data[0]["lat"]
        longitude = data[0]["lon"]
        forecast_response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric")
        forecast_data = forecast_response.json()
        
        # weather_map_response = requests.get(f'https://tile.openweathermap.org/map/temp_new/9/511/511.png?appid={api_key}')
        # with open(self.file_path, 'wb') as file:
        #     file.write(weather_map_response.content)
        icon_filename = weather_icons.get(forecast_data['weather'][0]['description'].lower(),"not-available.svg")

        return forecast_data,icon_filename
