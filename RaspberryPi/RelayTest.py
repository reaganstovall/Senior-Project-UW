from numpy import genfromtxt
import numpy as np
import RPi.GPIO as GPIO
import time
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

twoPinDigitalReadA = 18
twoPinDigitalReadB = 23

##GPIO.setup(twoPinDigitalReadA, GPIO.IN, GPIO.PUD_UP)
##GPIO.setup(twoPinDigitalReadB, GPIO.IN, GPIO.PUD_UP)

GPIO.setup(twoPinDigitalReadA, GPIO.OUT)
GPIO.setup(twoPinDigitalReadB, GPIO.OUT)

GPIO.output(twoPinDigitalReadA, GPIO.HIGH)
GPIO.output(twoPinDigitalReadB, GPIO.HIGH)

try:
    while(1):
        print("RELAY 1 ON - ")
        GPIO.output(twoPinDigitalReadA, GPIO.LOW)
        print("RELAY 2 ON - ")
        GPIO.output(twoPinDigitalReadB, GPIO.LOW)
        time.sleep(2)
        print("RELAY 1 OFF - ")
        GPIO.output(twoPinDigitalReadA, GPIO.HIGH)
        print("RELAY 2 OFF - ")
        GPIO.output(twoPinDigitalReadB, GPIO.HIGH)
        time.sleep(2)

    
except KeyboardInterrupt:
    GPIO.cleanup()
