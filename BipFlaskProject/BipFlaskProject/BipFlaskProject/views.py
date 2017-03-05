"""
Routes and views for the flask application along with switch functions.
"""

from datetime import datetime
from flask import render_template
from BipFlaskProject import app
#import RPi.GPIO as GPIO
import os

lightState = 'Off'

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        state=lightState,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/TurnOffSwitch')
def turnOff():
    """Turns off switch"""
    ChangeLightState(0)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        state=lightState,
    )

@app.route('/TurnOnSwitch')
def turnOn():
    """Turns on switch"""
    ChangeLightState(1)
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        state=lightState,
    )

def ChangeLightState(onOrOff):
    if onOrOff == 0:
        lightState = TurnOffSwitch()
    elif onOrOff == 1:
        lightState = TurnOnSwitch()
    return

def TurnOffSwitch():
    print 'Switch is off'
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(2, GPIO.OUT)
    #GPIO.output(2, True)
    return 'Off'

def TurnOnSwitch():
    print 'Switch is on'
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(2, GPIO.OUT)
    #GPIO.output(2, False)
    return 'On'