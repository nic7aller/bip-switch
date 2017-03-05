#import RPi.GPIO as GPIO

class LightSwitch(object):
    """Controls the light switch"""
    
    def __init__(self):
        self.lightState = 'Off'

    def ChangeLightState(self):
        if self.lightState == 'On':
            self.lightState = self.TurnOffSwitch()
        elif self.lightState == 'Off':
            self.lightState = self.TurnOnSwitch()
        return

    def TurnOffSwitch(self):
        print 'Switch is off'
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(7, GPIO.OUT)
        #GPIO.output(7, True)
        return 'Off'

    def TurnOnSwitch(self):
        print 'Switch is on'
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(7, GPIO.OUT)
        #GPIO.output(7, False)
        return 'On'
