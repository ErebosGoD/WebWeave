from flask import Flask, redirect, render_template, url_for, request, jsonify
from datetime import datetime, timedelta
from get_weather import WeatherForecast
from config import openweather_apikey

app = Flask(__name__, template_folder='templates')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather-forecast")
def weather():
    return render_template('weather.html')


@app.route("/time-calculator")
def time_calculator():
    return render_template("timecalculator.html")


@app.route("/get-weather", methods=["POST", "GET"])
def get_weather():
    location = request.form.get("location")
    current_forecast, icon_name,days = weather_forecast.get_weather_forecast(
        location,openweather_apikey)
    
    return render_template("forecast.html",current_forecast=current_forecast,svg_name=icon_name,location=location,days=days)


@app.route("/calculate-time", methods=["POST", "GET"])
def calculate_time():
    start_time = request.form.get("start-time")
    work_hours = int(request.form.get("work-hours"))
    work_minutes = int(request.form.get("work-minutes"))
    break_in_minutes = int(request.form.get("break-in-minutes"))
    overtime_hours = int(request.form.get("overtime-hours"))
    overtime_minutes = int(request.form.get("overtime-minutes"))
    work_hours = work_hours - overtime_hours
    work_minutes = work_minutes + break_in_minutes - overtime_minutes

    start_time_obj = datetime.strptime(start_time, '%H:%M')
    time_difference = timedelta(hours=work_hours, minutes=work_minutes)
    clock_off_time = start_time_obj + time_difference
    response_data = {"result": clock_off_time.strftime('%H:%M')}
    return jsonify(response_data)


if __name__ == "__main__":
    weather_forecast = WeatherForecast()
    app.run()
