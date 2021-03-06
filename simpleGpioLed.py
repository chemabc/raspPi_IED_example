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
GPIO.setup(7, GPIO.OUT) #GPIO 7 to OUT
GPIO.output(7, True) #Turn on GPIO 7


def blinkLed():
    print("Inciamos ejecucion...")
    iteracion = 0
    while iteracion < 5:
        GPIO.output(7, False)
        time.sleep(1) # 1 segundo
        GPIO.output(7, True)
        time.sleep(1) # 1 segundo
        iteracion += 1
    print("Ejecucion finalizada...")
    GPIO.cleanup()

blinkLed()

