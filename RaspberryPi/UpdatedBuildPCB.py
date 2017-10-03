from numpy import genfromtxt
import numpy as np
import RPi.GPIO as GPIO
import time
import Adafruit_ADS1x15

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
arraySize = 16

# ---------- ADC ----------
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3

# ---------- 16-to-1 MUX ----------
# 15 = PU 3V 5.1K
# 14 = PU 3V 51K
# 13 = PU 3V 100K
# 12 = PD 510K
# 11 = PD 1M
# 10 = PU 5V 5.1K
# 9 = PU 5V 51K
# 8 = PU 5V 100K
# 7 = CAP .1 UF
# 6 = PD 100
# 5 = PD 510
# 4 = PD 1K
# 3 = PD 5.1K
# 2 = PD 10K
# 1 = PD 51K
# 0 = PD 100K
sixteenS0 = 12
sixteenS1 = 16
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
eightAnalogA = 24
eightAnalogB = 23
eightAnalogC = 22

GPIO.setup(eightAnalogA, GPIO.OUT)
GPIO.setup(eightAnalogB, GPIO.OUT)
GPIO.setup(eightAnalogC, GPIO.OUT)

GPIO.output(eightAnalogA, GPIO.LOW)
GPIO.output(eightAnalogB, GPIO.LOW)
GPIO.output(eightAnalogC, GPIO.LOW)

# ---------- 8-to-1 Digital MUX ----------
eightDigitalA = 19
eightDigitalB = 13
eightDigitalC = 6
twoPinDigitalRead = 5

GPIO.setup(eightDigitalA, GPIO.OUT)
GPIO.setup(eightDigitalB, GPIO.OUT)
GPIO.setup(eightDigitalC, GPIO.OUT)
GPIO.setup(twoPinDigitalRead, GPIO.IN, GPIO.PUD_UP)

GPIO.output(eightDigitalA, GPIO.LOW)
GPIO.output(eightDigitalB, GPIO.LOW)
GPIO.output(eightDigitalC, GPIO.LOW)

# ---------- 2-to-1 Voltage MUX ----------
# HIGH = 3V
# LOW = 5V
twoVoltageSwitch = 27

GPIO.setup(twoVoltageSwitch, GPIO.OUT)

GPIO.output(twoVoltageSwitch, GPIO.LOW)

# ---------- 2-to-1 Analog/Digital MUX ----------
# HIGH = DIGITAL
# LOW = ANALOG
twoAnalogDigital= 25

GPIO.setup(twoAnalogDigital, GPIO.OUT)

GPIO.output(twoAnalogDigital, GPIO.LOW)

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

    GPIO.output(twoVoltageSwitch, GPIO.LOW)

    GPIO.output(twoAnalogDigital, GPIO.LOW)

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
    print('Reading ADS1x15 values, press Ctrl-C to quit...')
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
    print('-' * 37)
    values = [0]*4
    try:
        i = 0
        print("STARTING READINGS - ")
        while(1):
            if(sensorActive[i] == 1):
                print("SENSOR",i,"ON")
                
                if(sensorVoltage[i] == 3 or sensorVoltage[i] == 5):
                    if(sensorVoltage[i] == 3):
                        print("CHARGING 3 VOLTS")
                        GPIO.output(twoVoltageSwitch, GPIO.HIGH)
                    else:
                        print("CHARGING 5 VOLTS")
                        GPIO.output(twoVoltageSwitch, GPIO.LOW)
                    time.sleep(1)

                    if(sensorType[i] == 1):
                        print("ANALOG")

                        if(sensorPin[i] == 3):
                            print("3 PIN")
                            muxDeciderEightAnalog(i)
                            GPIO.output(twoAnalogDigital, GPIO.HIGH)
                            time.sleep(1)
                            for j in range(4):
                                values[j] = adc.read_adc(j, gain=GAIN)
                            print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
                            
                        elif(sensorPin[i] == 2):
                            print("2 PIN")
                            muxDeciderEightAnalog(i)
                            GPIO.output(twoAnalogDigital, GPIO.LOW)
                            muxDeciderSixteenResistors(sensorResistor[i])
                            for j in range(4):
                                values[j] = adc.read_adc(j, gain=GAIN)
                            print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
                            
                    elif(sensorType[i] == 2):
                        print("DIGITAL")
                        
                        if(sensorPin[i] == 3):
                            print("3 PIN")
                            muxDeciderEightDigital(i)
                            time.sleep(1)
                            print("VALUE - ",GPIO.input(twoPinDigitalRead))

                        elif(sensorPin[i] == 2):
                            print("2 PIN")
                            muxDeciderEightDigital(i)
                            if(sensorResistor[i] != 0):
                                muxDeciderSixteenResistors(sensorResistor[i])
                            time.sleep(1)
                            print("VALUE - ",GPIO.input(twoPinDigitalRead))

                elif(sensorVoltage[i] == 1):
                    print("GROUND INPUT")
                    time.sleep(1)
                    
                    if(sensorType[i] == 1):
                        print("ANALOG")

                        if(sensorPin[i] == 2):
                            print("2 PIN")
                            muxDeciderEightAnalog(i)
                            GPIO.output(twoAnalogDigital, GPIO.LOW)
                            muxDeciderSixteenResistors(sensorResistor[i])
                            for j in range(4):
                                values[j] = adc.read_adc(j, gain=GAIN)
                            print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
                            
                    elif(sensorType[i] == 2):
                        print("DIGITAL")
                            
                        if(sensorPin[i] == 2):
                            print("2 PIN")
                            muxDeciderEightDigital(i)
                            if(sensorResistor[i] != 0):
                                muxDeciderSixteenResistors(sensorResistor[i])
                            time.sleep(1)
                            print("VALUE - ",GPIO.input(twoPinDigitalRead))


            else:
                print("SENSOR",i,"INACTIVE")
                
            if(i < 7):
                i += 1
            else:
                i = 0

            outputReset()
            time.sleep(.5)
            

    except KeyboardInterrupt:
        outputReset()
        GPIO.cleanup()

def muxDeciderEightAnalog(i):
    if(i == 0):
        GPIO.output(eightAnalogA, GPIO.HIGH)
        GPIO.output(eightAnalogB, GPIO.HIGH)
        GPIO.output(eightAnalogC, GPIO.LOW)

    elif(i == 1):
        GPIO.output(eightAnalogA, GPIO.LOW)
        GPIO.output(eightAnalogB, GPIO.LOW)
        GPIO.output(eightAnalogC, GPIO.LOW)

    elif(i == 2):
        GPIO.output(eightAnalogA, GPIO.HIGH)
        GPIO.output(eightAnalogB, GPIO.LOW)
        GPIO.output(eightAnalogC, GPIO.LOW)

    elif(i == 3):
        GPIO.output(eightAnalogA, GPIO.LOW)
        GPIO.output(eightAnalogB, GPIO.HIGH)
        GPIO.output(eightAnalogC, GPIO.LOW)

    elif(i == 4):
        GPIO.output(eightAnalogA, GPIO.LOW)
        GPIO.output(eightAnalogB, GPIO.LOW)
        GPIO.output(eightAnalogC, GPIO.HIGH)

    elif(i == 5):
        GPIO.output(eightAnalogA, GPIO.LOW)
        GPIO.output(eightAnalogB, GPIO.HIGH)
        GPIO.output(eightAnalogC, GPIO.HIGH)

    elif(i == 6):
        GPIO.output(eightAnalogA, GPIO.HIGH)
        GPIO.output(eightAnalogB, GPIO.HIGH)
        GPIO.output(eightAnalogC, GPIO.HIGH)

    elif(i == 7):
        GPIO.output(eightAnalogA, GPIO.HIGH)
        GPIO.output(eightAnalogB, GPIO.LOW)
        GPIO.output(eightAnalogC, GPIO.HIGH)

def muxDeciderEightDigital(i):
    if(i == 0):
        GPIO.output(eightDigitalA, GPIO.HIGH)
        GPIO.output(eightDigitalB, GPIO.HIGH)
        GPIO.output(eightDigitalC, GPIO.LOW)

    elif(i == 1):
        GPIO.output(eightDigitalA, GPIO.LOW)
        GPIO.output(eightDigitalB, GPIO.LOW)
        GPIO.output(eightDigitalC, GPIO.LOW)

    elif(i == 2):
        GPIO.output(eightDigitalA, GPIO.HIGH)
        GPIO.output(eightDigitalB, GPIO.LOW)
        GPIO.output(eightDigitalC, GPIO.LOW)

    elif(i == 3):
        GPIO.output(eightDigitalA, GPIO.HIGH)
        GPIO.output(eightDigitalB, GPIO.LOW)
        GPIO.output(eightDigitalC, GPIO.HIGH)
        
    elif(i == 4):
        GPIO.output(eightDigitalA, GPIO.LOW)
        GPIO.output(eightDigitalB, GPIO.HIGH)
        GPIO.output(eightDigitalC, GPIO.LOW)

    elif(i == 5):
        GPIO.output(eightDigitalA, GPIO.HIGH)
        GPIO.output(eightDigitalB, GPIO.HIGH)
        GPIO.output(eightDigitalC, GPIO.HIGH)

    elif(i == 6):
        GPIO.output(eightDigitalA, GPIO.LOW)
        GPIO.output(eightDigitalB, GPIO.HIGH)
        GPIO.output(eightDigitalC, GPIO.HIGH)

    elif(i == 7):
        GPIO.output(eightDigitalA, GPIO.LOW)
        GPIO.output(eightDigitalB, GPIO.LOW)
        GPIO.output(eightDigitalC, GPIO.HIGH)

def muxDeciderSixteenResistors(i):
    binaryResult = format(int(i), "04b")
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
