"""
Routes and views for the flask application along with switch functions.
"""

from flask import render_template
from BipFlaskProject import app
from LightSwitch import LightSwitch

lightSwitch = LightSwitch()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        state = lightSwitch.lightState,
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        message = 'Your application description page.'
    )

@app.route('/TurnSwitch')
def turnSwitch():
    """Turns on or off switch"""
    lightSwitch.ChangeLightState()
    return render_template(
        'index.html',
        state = lightSwitch.lightState,
    )
