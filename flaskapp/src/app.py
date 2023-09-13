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
    api_key = "deb143ec8c4f97aab4a9368f770ef498"
    location = request.form.get('location')
    zipcode = request.form.get('zipcode')
    response = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit={1}&appid={api_key}")
    data = response.json()
    print(data)
    return data


if __name__ == "__main__":
    app.run(debug=True)
