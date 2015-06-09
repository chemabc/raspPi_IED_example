# -*- coding: utf-8 -*-
'''
https://geekytheory.com/tutorial-raspberry-pi-gpio-parte-1-control-de-un-led/
https://geekytheory.com/tutorial-raspberry-pi-gpio-parte-2-control-de-leds-con-python/
INSTALAR LIBRERIA GPIO:
sudo apt-get install python-dev python-rpì.gpio
En el terminal/consola linux, escribir:


'''
import time
import RPi.GPIO as GPIO #import GPIO library

GPIO.setmode(GPIO.BOARD) #use board pin numering
GPIO.setup(7, GPIO.IN) #GPIO 7 to OUT

currentInput = GPIO.input(7)
lastInput = currentInput

while (True):
    if not GPIO.input(7):
        print("button pressed")
    '''
    currentInput = GPIO.input(7)
    if(currentInput is not lastInput)
        print("Cambio to: " + str(currentInput))
        lastInput = currentInput
    '''
GPIO.cleanup()



