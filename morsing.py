import RPi.GPIO as GPIO
import time


def turnComponentOff(PinNumber):
    GPIO.output(PinNumber,GPIO.LOW)

def turnComponentOn(PinNumber):
    GPIO.output(PinNumber,GPIO.HIGH)

def morse(morsePhrase):   
        for x in morsePhrase:
	    # short Signal
            if(x == '0'):
                turnComponentOn(17)
                turnComponentOn(22)
                time.sleep(0.5)
                turnComponentOff(17)
                turnComponentOff(22)
                time.sleep(1)
	    # long Signal
            else:
                turnComponentOn(17)
                turnComponentOn(22)
                time. sleep(1)
                turnComponentOff(17)
                turnComponentOff(22)
                time.sleep(1)
    
            
            



    
   
