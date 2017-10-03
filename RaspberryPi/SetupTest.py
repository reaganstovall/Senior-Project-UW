from numpy import genfromtxt
import numpy as np
import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ---------- ADC ----------
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# ---------- 16-to-1 MUX ----------
# 15 = PD 100
# 14 = PD 220
# 13 = PD 1K
# 12 = PD 4.7K
# 11 = PD 10K
# 10 = PD 47K
# 9 = PD 100K
# 8 = PD 1M
# 7 = PU 3V 4.7K
# 6 = PU 3V 22K
# 5 = PU 3V 47K
# 4 = PU 3V 100K
# 3 = PU 5V 4.7K
# 2 = PU 5V 22K
# 1 = PU 5V 47K
# 0 = PU 5V 100K
sixteenS0 = 26
sixteenS1 = 19
sixteenS2 = 21
sixteenS3 = 20

GPIO.setup(sixteenS0, GPIO.OUT)
GPIO.setup(sixteenS1, GPIO.OUT)
GPIO.setup(sixteenS2, GPIO.OUT)
GPIO.setup(sixteenS3, GPIO.OUT)

GPIO.output(sixteenS0, GPIO.LOW)
GPIO.output(sixteenS1, GPIO.LOW)
GPIO.output(sixteenS2, GPIO.LOW)
GPIO.output(sixteenS3, GPIO.LOW)

# ---------- 8-to-1 Analog MUX ----------
eightAnalogA = 5
eightAnalogB = 6
eightAnalogC = 13

GPIO.setup(eightAnalogA, GPIO.OUT)
GPIO.setup(eightAnalogB, GPIO.OUT)
GPIO.setup(eightAnalogC, GPIO.OUT)

GPIO.output(eightAnalogA, GPIO.LOW)
GPIO.output(eightAnalogB, GPIO.LOW)
GPIO.output(eightAnalogC, GPIO.LOW)

# ---------- 8-to-1 Digital MUX ----------
eightDigitalA = 10
eightDigitalB = 9
eightDigitalC = 11
twoPinDigitalRead = 17

GPIO.setup(eightDigitalA, GPIO.OUT)
GPIO.setup(eightDigitalB, GPIO.OUT)
GPIO.setup(eightDigitalC, GPIO.OUT)
GPIO.setup(twoPinDigitalRead, GPIO.IN, GPIO.PUD_UP)

GPIO.output(eightDigitalA, GPIO.LOW)
GPIO.output(eightDigitalB, GPIO.LOW)
GPIO.output(eightDigitalC, GPIO.LOW)

# ---------- 2-to-1 Voltage MUX ----------
twoVoltageA = 27
twoVoltageB = 22

GPIO.setup(twoVoltageA, GPIO.OUT)
GPIO.setup(twoVoltageB, GPIO.OUT)

GPIO.output(twoVoltageA, GPIO.LOW)
GPIO.output(twoVoltageB, GPIO.LOW)

# ---------- 2-to-1 Analog/Digital MUX ----------
twoAnalogDigitalA = 12
twoAnalogDigitalB = 16

GPIO.setup(twoAnalogDigitalA, GPIO.OUT)
GPIO.setup(twoAnalogDigitalB, GPIO.OUT)

GPIO.output(twoAnalogDigitalA, GPIO.LOW)
GPIO.output(twoAnalogDigitalB, GPIO.LOW)

def outputReset():
    GPIO.output(sixteenS0, GPIO.LOW)
    GPIO.output(sixteenS1, GPIO.LOW)
    GPIO.output(sixteenS2, GPIO.LOW)
    GPIO.output(sixteenS3, GPIO.LOW)

    GPIO.output(eightAnalogA, GPIO.LOW)
    GPIO.output(eightAnalogB, GPIO.LOW)
    GPIO.output(eightAnalogC, GPIO.LOW)

    GPIO.output(eightDigitalA, GPIO.LOW)
    GPIO.output(eightDigitalB, GPIO.LOW)
    GPIO.output(eightDigitalC, GPIO.LOW)

    GPIO.output(twoVoltageA, GPIO.LOW)
    GPIO.output(twoVoltageB, GPIO.LOW)

    GPIO.output(twoAnalogDigitalA, GPIO.LOW)
    GPIO.output(twoAnalogDigitalB, GPIO.LOW)

try:
    while(1):
##        print("5V -> Analog Sensor -> 8 MUX -> ADC")
##        
##        GPIO.output(twoVoltageA, GPIO.HIGH)
##
##        GPIO.output(eightAnalogA, GPIO.LOW)
##        GPIO.output(eightAnalogB, GPIO.LOW)
##        GPIO.output(eightAnalogC, GPIO.HIGH)
##        
##        print(mcp.read_adc(0))
##        time.sleep(1)
##
##        outputReset()

##        print("5V -> Analog Sensor -> 8 MUX -> 2 MUX -> 16 MUX -> ADC")
##        
##        GPIO.output(twoVoltageA, GPIO.HIGH)
##
##        GPIO.output(eightAnalogA, GPIO.LOW)
##        GPIO.output(eightAnalogB, GPIO.LOW)
##        GPIO.output(eightAnalogC, GPIO.HIGH)
##
##        GPIO.output(sixteenS0, GPIO.LOW)
##        GPIO.output(sixteenS1, GPIO.LOW )
##        GPIO.output(sixteenS2, GPIO.LOW)
##        GPIO.output(sixteenS3, GPIO.LOW)
##
##        GPIO.output(twoAnalogDigitalA, GPIO.HIGH)
##        
##        print(mcp.read_adc(0))
##        time.sleep(1)
##
##        outputReset()

        # ANALOG
        print("GND -> Analog Sensor -> 8 MUX -> 2 MUX -> 16 MUX -> ADC")
        
        GPIO.output(twoVoltageA, GPIO.HIGH)

        GPIO.output(eightAnalogA, GPIO.LOW)
        GPIO.output(eightAnalogB, GPIO.LOW)
        GPIO.output(eightAnalogC, GPIO.HIGH)

        GPIO.output(sixteenS0, GPIO.LOW)
        GPIO.output(sixteenS1, GPIO.LOW )
        GPIO.output(sixteenS2, GPIO.LOW)
        GPIO.output(sixteenS3, GPIO.LOW)

        GPIO.output(twoAnalogDigitalA, GPIO.HIGH)
        
        print(mcp.read_adc(0))
        time.sleep(1)

        outputReset()

        # DIGITAL
        print("5V -> Digital Sensor -> 8 MUX -> Read")
        
        GPIO.output(twoVoltageA, GPIO.HIGH)

        GPIO.output(eightDigitalA, GPIO.LOW)
        GPIO.output(eightDigitalB, GPIO.LOW)
        GPIO.output(eightDigitalC, GPIO.HIGH)
        
        print(GPIO.input(twoPinDigitalRead))
        time.sleep(1)

        outputReset()

except KeyboardInterrupt:
    GPIO.output(sixteenS0, GPIO.LOW)
    GPIO.output(sixteenS1, GPIO.LOW)
    GPIO.output(sixteenS2, GPIO.LOW)
    GPIO.output(sixteenS3, GPIO.LOW)

    GPIO.output(eightAnalogA, GPIO.LOW)
    GPIO.output(eightAnalogB, GPIO.LOW)
    GPIO.output(eightAnalogC, GPIO.LOW)

    GPIO.output(eightDigitalA, GPIO.LOW)
    GPIO.output(eightDigitalB, GPIO.LOW)
    GPIO.output(eightDigitalC, GPIO.LOW)

    GPIO.output(twoVoltageA, GPIO.LOW)
    GPIO.output(twoVoltageB, GPIO.LOW)

    GPIO.output(twoAnalogDigitalA, GPIO.LOW)
    GPIO.output(twoAnalogDigitalB, GPIO.LOW)

    GPIO.cleanup()
