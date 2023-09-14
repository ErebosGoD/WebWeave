from flask import Flask, redirect, render_template, url_for, request
import requests

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather-forecast")
def weather():
    return render_template('weather.html')


@app.route("/get-weather", methods=["POST", "GET"])
def get_weather():
    api_key = "key"
    location = request.form.get('location')
    location_response = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit={1}&appid={api_key}")
    data = location_response.json()
    latitude = data[0]["lat"]
    longitude = data[0]["lon"]
    forecast_response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}")
    forecast_data = forecast_response.json()

    return forecast_data


if __name__ == "__main__":
    app.run(debug=True)
