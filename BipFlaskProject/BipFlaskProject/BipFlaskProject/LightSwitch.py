import RPi.GPIO as GPIO

class LightSwitch(object):
    """Controls the light switch"""
    
    def __init__(self):
        self.lightState = 'Off'
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)

    def ChangeLightState(self):
        if self.lightState == 'On':
            self.lightState = self.TurnOffSwitch()
        elif self.lightState == 'Off':
            self.lightState = self.TurnOnSwitch()
        return

    def TurnOffSwitch(self):
        print 'Switch is off'
        GPIO.output(4, True)
        return 'Off'

    def TurnOnSwitch(self):
        print 'Switch is on'
        GPIO.output(4, False)
        return 'On'
