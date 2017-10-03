import numpy as np
from numpy import genfromtxt
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
threePinDigitalRead = 17

GPIO.setup(eightDigitalA, GPIO.OUT)
GPIO.setup(eightDigitalB, GPIO.OUT)
GPIO.setup(eightDigitalC, GPIO.OUT)
GPIO.setup(threePinDigitalRead, GPIO.IN, GPIO.PUD_UP)

GPIO.output(eightDigitalA, GPIO.LOW)
GPIO.output(eightDigitalB, GPIO.LOW)
GPIO.output(eightDigitalC, GPIO.LOW)

# ---------- 2-to-1 Voltage MUX ----------
twoVoltage3 = 22
twoVoltage5 = 27

GPIO.setup(twoVoltage3, GPIO.OUT)
GPIO.setup(twoVoltage5, GPIO.OUT)

GPIO.output(twoVoltage3, GPIO.LOW)
GPIO.output(twoVoltage5, GPIO.LOW)

# ---------- 2-to-1 Analog/Digital MUX ----------
twoAnalogDigitalA = 12
twoAnalogDigitalD = 16

GPIO.setup(twoAnalogDigitalA, GPIO.OUT)
GPIO.setup(twoAnalogDigitalD, GPIO.OUT)

GPIO.output(twoAnalogDigitalA, GPIO.LOW)
GPIO.output(twoAnalogDigitalD, GPIO.LOW)

# ---------- Sensor Settings ----------
arraySize = 16
sensorActive = []
sensorType = []
sensorPin = []
sensorResistor = []
sensorVoltage = []
boolResult = []

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

    GPIO.output(twoVoltage3, GPIO.LOW)
    GPIO.output(twoVoltage5, GPIO.LOW)

    GPIO.output(twoAnalogDigitalA, GPIO.LOW)
    GPIO.output(twoAnalogDigitalD, GPIO.LOW)

def sensorFileSetup():
    global sensorActive
    global sensorType
    global sensorPin
    global sensorVoltage
    global sensorResistor
    data = genfromtxt("sensordata.txt", delimiter=",")

    sensorActive = data[0] # 1 = ON
    sensorType = data[1] # 1 = ANALOG, 2 = DIGITAL, 3 = MISC
    sensorPin = data[2] # 2 PIN OR 3 PIN
    sensorVoltage = data[3] # 3 VOLTS(3) OR 5 VOLTS(5) OR GROUND(1)
    sensorResistor = data[4] # RESISTOR TYPE

    print(sensorActive)
    print(sensorType)
    print(sensorPin)
    print(sensorVoltage)
    print(sensorResistor)

def sensorInitialization():
    for i in range(arraySize):
        #print(sensorActive[i])
        if(sensorActive[i] == 1):
            print("SENSOR",i,"ON")
            #if(sensorType == 3):

def sensorRead():
    try:
        i = 0
        print("STARTING READINGS - ")
        while(1):
            if(sensorActive[i] == 1):
                print("SENSOR",i,"ON")
                
                if(sensorVoltage[i] == 3 or sensorVoltage[i] == 5):
                    if(sensorVoltage[i] == 3):
                        print("CHARGING 3 VOLTS")
                        GPIO.output(twoVoltage3, GPIO.HIGH)
                        GPIO.output(twoVoltage5, GPIO.LOW)
                    else:
                        print("CHARGING 5 VOLTS")
                        GPIO.output(twoVoltage5, GPIO.HIGH)
                        GPIO.output(twoVoltage3, GPIO.LOW)
                    time.sleep(1)

                    if(sensorType[i] == 1):
                        print("ANALOG")

                        if(sensorPin[i] == 3):
                            print("3 PIN")
                            muxDeciderEightAnalog(i)
                            GPIO.output(twoAnalogDigitalD, GPIO.HIGH)
                            time.sleep(1)
                            print("VALUE - ",mcp.read_adc(0))
                            
                        elif(sensorPin[i] == 2):
                            print("2 PIN")
                            muxDeciderEightAnalog(i)
                            GPIO.output(twoAnalogDigitalA, GPIO.HIGH)
                            muxDeciderSixteenResistors(i)
                            
                    elif(sensorType[i] == 2):
                        print("DIGITAL")
                        
                        if(sensorPin[i] == 3):
                            print("3 PIN")
                            muxDeciderEightDigital(i)
                            time.sleep(1)
                            print("VALUE - ",GPIO.input(threePinDigitalRead))

                        elif(sensorPin[i] == 2):
                            print("2 PIN")
                            muxDeciderEightDigital(i)
                            if(sensorResistor[i] != 0):
                                muxDeciderSixteenResistors(i)
                            time.sleep(1)
                            print("VALUE - ",GPIO.input(threePinDigitalRead))

                elif(sensorVoltage[i] == 1):
                    print("GROUND INPUT")
                    time.sleep(1)
                    
                    if(sensorType[i] == 1):
                        print("ANALOG")

                        if(sensorPin[i] == 2):
                            print("2 PIN")
                            muxDeciderEightAnalog(i)
                            GPIO.output(twoAnalogDigitalA, GPIO.HIGH)
                            muxDeciderSixteenResistors(i)
                            
                    elif(sensorType[i] == 2):
                        print("DIGITAL")
                            
                        if(sensorPin[i] == 2):
                            print("2 PIN")
                            muxDeciderEightDigital(i)
                            if(sensorResistor[i] != 0):
                                muxDeciderSixteenResistors(i)
                            time.sleep(1)
                            print("VALUE - ",GPIO.input(threePinDigitalRead))


            else:
                print("SENSOR",i,"INACTIVE")
                
            if(i < 4):
                i += 1
            else:
                i = 0

            outputReset()
            time.sleep(.5)
            

    except KeyboardInterrupt:
        outputReset()
        GPIO.cleanup()

def muxDeciderEightAnalog(i):
    binaryResult = format(i, "03b")
##    print(binaryResult[2])
##    print(binaryResult[1])
##    print(binaryResult[0])
##    print(binaryResult)
        
    if(binaryResult[2] == '0'):
        GPIO.output(eightAnalogA, GPIO.LOW)
    else:
        GPIO.output(eightAnalogA, GPIO.HIGH)
        
    if(binaryResult[1] == '0'):
        GPIO.output(eightAnalogB, GPIO.LOW)
    else:
        GPIO.output(eightAnalogB, GPIO.HIGH)
        
    if(binaryResult[0] == '0'):
        GPIO.output(eightAnalogC, GPIO.LOW)
    else:
        GPIO.output(eightAnalogC, GPIO.HIGH)

def muxDeciderEightDigital(i):
    binaryResult = format(i, "03b")
##    print(binaryResult[2])
##    print(binaryResult[1])
##    print(binaryResult[0])
##    print(binaryResult)
        
    if(binaryResult[2] == '0'):
        GPIO.output(eightDigitalA, GPIO.LOW)
    else:
        GPIO.output(eightDigitalA, GPIO.HIGH)
        
    if(binaryResult[1] == '0'):
        GPIO.output(eightDigitalB, GPIO.LOW)
    else:
        GPIO.output(eightDigitalB, GPIO.HIGH)
        
    if(binaryResult[0] == '0'):
        GPIO.output(eightDigitalC, GPIO.LOW)
    else:
        GPIO.output(eightDigitalC, GPIO.HIGH)

def muxDeciderSixteenResistors(i):
    binaryResult = format(i, "04b")
##    print(binaryResult[3])
##    print(binaryResult[2])
##    print(binaryResult[1])
##    print(binaryResult[0])
##    print(binaryResult)

    if(binaryResult[3] == '0'):
        GPIO.output(sixteenS0, GPIO.LOW)
    else:
        GPIO.output(sixteenS0, GPIO.HIGH)
        
    if(binaryResult[2] == '0'):
        GPIO.output(sixteenS1, GPIO.LOW)
    else:
        GPIO.output(sixteenS1, GPIO.HIGH)
        
    if(binaryResult[1] == '0'):
        GPIO.output(sixteenS2, GPIO.LOW)
    else:
        GPIO.output(sixteenS2, GPIO.HIGH)
        
    if(binaryResult[0] == '0'):
        GPIO.output(sixteenS3, GPIO.LOW)
    else:
        GPIO.output(sixteenS3, GPIO.HIGH)

            
sensorFileSetup()
sensorInitialization()
sensorRead()
