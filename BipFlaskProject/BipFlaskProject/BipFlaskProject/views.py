"""
Routes and views for the flask application along with switch functions.
"""

from flask import render_template
from BipFlaskProject import app
from LightSwitch import LightSwitch
import forecastio

lightSwitch = LightSwitch()

api_key = "e59dd0570c87555e9219188605bb324c"
lat = -31.967819
lng = 40.00404
forecast = forecastio.load_forecast(api_key, lat, lng)

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    forecast = forecastio.load_forecast(api_key, lat, lng)
    temp = str(forecast.currently().temperature)
    return render_template(
        'index.html',
        state = lightSwitch.lightState,
        weather = forecast.currently().summary + ', ' + temp + '&deg;F',
        precip = forecast.currently().precipProbability
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
    )

@app.route('/TurnSwitch')
def turnSwitch():
    """Turns on or off switch"""
    lightSwitch.ChangeLightState()
    forecast = forecastio.load_forecast(api_key, lat, lng)
    temp = str(forecast.currently().temperature)
    return render_template(
        'index.html',
        state = lightSwitch.lightState,
        weather = forecast.currently().icon + forecast.currently().summary + ', ' + temp,
        precip = forecast.currently().precipProbability
    )
