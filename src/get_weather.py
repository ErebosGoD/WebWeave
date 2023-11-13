import requests
from weathericondict import weather_icons
import os
from datetime import datetime


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
        current_forecast_response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric")
        current_forecast_data = current_forecast_response.json()
        
        forecast_response = requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={api_key}&units=metric")
        forecast_data = forecast_response.json()
        #print(forecast_data['list'])
        # Extrahiere die Liste der Wetterdaten
        weather_list = forecast_data["list"]

        # Initialisiere ein leeres Dictionary, um die "day" Objekte pro Tag zu speichern
        days_dict = {}

        # Iteriere durch die Wetterdaten und extrahiere die "day" Objekte für die mittlere Uhrzeit pro Tag
        for entry in weather_list:
            # Konvertiere den Unix-Zeitstempel in ein lesbares Datum
            date_time = datetime.utcfromtimestamp(entry["dt"])
            
            # Extrahiere die Stunde aus dem Datum
            hour = date_time.hour
            
            # Überprüfe, ob die Stunde der mittleren Uhrzeit entspricht (z.B. 15 Uhr)
            if hour == 15:
                # Extrahiere das Datum (ohne Uhrzeit)
                date = date_time.date()

                # Erzeuge ein "day" Objekt für diesen Tag
                day_object = {
                    "dt": entry["dt_txt"],
                    "main": entry["main"],
                    "weather": entry["weather"],
                    "wind":entry["wind"],
                    "icon_filename": weather_icons.get(entry["weather"][0]["description"].lower(), "not-available.svg")
                }

                # Speichere das "day" Objekt im Dictionary, wobei das Datum als Schlüssel verwendet wird
                days_dict[date] = day_object

        # Konvertiere das Dictionary in eine Liste, um die "day" Objekte zu erhalten
        days = list(days_dict.values())
        

        current_icon_filename = weather_icons.get(current_forecast_data['weather'][0]['description'].lower(),"not-available.svg")
        return current_forecast_data,current_icon_filename,days
