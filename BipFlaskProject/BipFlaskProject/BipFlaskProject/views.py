"""
Routes and views for the flask application along with switch functions.
"""

from datetime import datetime
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
        title = 'Home Page',
        year = datetime.now().year,
        state = lightSwitch.lightState,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title = 'Contact',
        year = datetime.now().year,
        message = 'Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title = 'About',
        year = datetime.now().year,
        message = 'Your application description page.'
    )

@app.route('/TurnSwitch')
def turnSwitch():
    """Turns on or off switch"""
    lightSwitch.ChangeLightState()
    return render_template(
        'index.html',
        title = 'Home Page',
        year = datetime.now().year,
        state = lightSwitch.lightState,
    )
