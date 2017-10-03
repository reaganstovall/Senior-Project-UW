from numpy import genfromtxt
import numpy as np
import RPi.GPIO as GPIO
import Adafruit_ADS1x15
import BuildSettings
import urllib2
import urllib
import smbus
import time
import sys
import os

# ---------- Miscellaneous ----------
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
startTime = time.time()
currentTime = startTime

# ---------- Database ----------
#HOST is my sql.hostinger.in
#USER u750059057_peeps
#PASSWORD klonitsko1
#DATABASE u750059057_ams
databaseArray = {}
url = 'http://automateuw.pe.hu/automationstation/addOBJ.php'

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

# ---------- 8 Channel Relay/Motor Controller (GPIO Extender) ----------
bus = smbus.SMBus(1)
address = 0x27

bus.write_byte_data(address, 0x06, 0x00)
bus.write_byte_data(address, 0x07, 0x00)
bus.write_byte_data(address, 0x02, 0xff)
bus.write_byte_data(address, 0x03, 0x00)

#INDEX 0 IS RELAY 7
#INDEX 1 IS RELAY 6
#INDEX 2 IS RELAY 5
#INDEX 3 IS RELAY 4
#INDEX 4 IS RELAY 3
#INDEX 5 IS RELAY 2
#INDEX 6 IS RELAY 1
#INDEX 7 IS RELAY 0
relayConfig = [1,1,1,1,1,1,1,1]

#INDEX 0 IS MOTOR 3
#INDEX 1 IS ENABLE
#INDEX 2 IS MOTOR 2
#INDEX 3 IS MOTOR 1
#INDEX 4 IS MOTOR 4
motorConfig = [0,1,0,0,0,0,0,0]

tempString = ""
tempStringArray= ""

# Function that will reset every GPIO output to LOW
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

# Function to print out the active sensors, Analog and Digital
def sensorInitialization():
    print("ANALOG - ")
    for i in range(len(BuildSettings.PAP)):
        if(BuildSettings.PAP[i] == 1):
            print("SENSOR",i,"ON")
            
    print("DIGITAL - ")
    for i in range(len(BuildSettings.PDP)):
        if(BuildSettings.PDP[i] == 1):
            print("SENSOR",i,"ON")

# Function to choose the correct Analog 8 MUX channel based on input
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

# Function to choose the correct Digital 8 MUX channel based on input
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

# Function to choose the correct Resistor 16 MUX channel based on input
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

# Function to convert the relayConfig array into a format to be written to I2C
def relaySend():
    tempStringArray = map(str, relayConfig)
    tempString = ''.join(tempStringArray)
    tempHex = hex(int(tempString,2))
    relayValue = int(tempHex, 16)
    bus.write_byte_data(address, 0x02, relayValue)

# Function to convert the motorConfig array into a format to be written to I2C
def motorControllerSend():
    tempStringArray = map(str, motorConfig)
    tempString = ''.join(tempStringArray)
    tempHex = hex(int(tempString,2))
    motorValue = int(tempHex, 16)
    bus.write_byte_data(address, 0x03, motorValue)

# Function to send the current databaseArray to the Database
def databaseSend(databaseArray):
    data = urllib.urlencode(databaseArray)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_page = response.read()

# Function to check the predefined FNC_List to see whether the functions are satisfied
# or not. If the function is satisfied then it will perform the appropriate action.
def functionCheck(sensorResults):
    # Update currentTime to be used for function timings
    currentTime = time.time() - startTime
    print("CURRENT TIME - ",currentTime)
    sensorResults = sensorResults.split(",")
    functionSatisfied = False

    for i in range(len(BuildSettings.FNC_List)):
        print("")
        print("FUNCTION " ,i)
        print(BuildSettings.FNC_List[i])

        # If StartTime is the beginning: start
        if(BuildSettings.FNC_List[i][0] == 0 or BuildSettings.FNC_List[i][0] < currentTime):
            print("START TIME SATISFIED")

            # If EndTime has passed: stop
            if(BuildSettings.FNC_List[i][1] < currentTime):
                print("STOP RUNNING")

            # If EndTime has not passed: continue
            else:
                print("START/CONTINUE RUNNING")

                # Primary Analog
                if(BuildSettings.FNC_List[i][6][0] == 1):
                    sensorValue = sensorResults[BuildSettings.FNC_List[i][6][1]]
                    
                    # Greater Than
                    if(BuildSettings.FNC_List[i][4] == 1):
                        if(sensorValue > BuildSettings.FNC_List[i][5]):
                            functionSatisfied = True

                    # Less Than
                    elif(BuildSettings.FNC_List[i][4] == 2):
                        if(sensorValue < BuildSettings.FNC_List[i][5]):
                            functionSatisfied = True
                            
                            
                # Primary Digital
                elif(BuildSettings.FNC_List[i][6][0] == 2):
                    sensorValue = sensorResults[BuildSettings.FNC_List[i][6][1] + 8]

                    # Digital Low
                    if(BuildSettings.FNC_List[i][5] == 1):
                        if(sensorValue == 0):
                            functionSatisfied = True
                                                        

                    # Digital High
                    elif(BuildSettings.FNC_List[i][5] == 2):
                        if(sensorValue == 1):
                            functionSatisfied = True
                            
        else:
            print("TIME OUT OF RANGE")

        # If functionSatisfied is True, do the appropriate function
        if(functionSatisfied == True):
            print("Function Satisfied - ", functionSatisfied)

            # Motors 
            if(BuildSettings.FNC_List[i][2][0] == 1):
                print("PRIMARY MOTOR")

                # Motor 1
                if(BuildSettings.FNC_List[i][2][1] == 0):
                    # Single Motor On/Off
                    if(BuildSettings.FNC_List[i][3] == 1):
                        motorConfig[3] = 1
                    elif(BuildSettings.FNC_List[i][3] == 0):
                        motorConfig[3] = 0

                    # Double Motor Forward/Reverse
                    elif(BuildSettings.FNC_List[i][3] == 2):
                        motorConfig[3] = 0
                        motorConfig[2] = 1
                    elif(BuildSettings.FNC_List[i][3] == 3):
                        motorConfig[3] = 1
                        motorConfig[2] = 0

                # Motor 2
                elif(BuildSettings.FNC_List[i][2][1] == 1):
                    # Single Motor On/Off
                    if(BuildSettings.FNC_List[i][3] == 1):
                        motorConfig[2] = 1
                    elif(BuildSettings.FNC_List[i][3] == 0):
                        motorConfig[2] = 0

                # Motor 3
                elif(BuildSettings.FNC_List[i][2][1] == 2):
                    # Single Motor On/Off
                    if(BuildSettings.FNC_List[i][3] == 1):
                        motorConfig[0] = 1
                    elif(BuildSettings.FNC_List[i][3] == 0):
                        motorConfig[0] = 0

                    # Double Motor Forward/Reverse
                    elif(BuildSettings.FNC_List[i][3] == 2):
                        motorConfig[0] = 0
                        motorConfig[4] = 1
                    elif(BuildSettings.FNC_List[i][3] == 3):
                        motorConfig[0] = 1
                        motorConfig[4] = 0

                # Motor 4
                elif(BuildSettings.FNC_List[i][2][1] == 3):
                    # Single Motor On/Off
                    if(BuildSettings.FNC_List[i][3] == 1):
                        motorConfig[4] = 1
                    elif(BuildSettings.FNC_List[i][3] == 0):
                        motorConfig[4] = 0

            # 12V Relay Side 4-1
            elif(BuildSettings.FNC_List[i][2][0] == 3):
                print("PRIMARY 12V RELAY")

                # Relay Port 4
                if(BuildSettings.FNC_List[i][2][1] == 3):
                    if(BuildSettings.FNC_List[i][3] == 4):
                        relayConfig[4] = 0
                    elif(BuildSettings.FNC_List[i][3] == 5):
                        relayConfig[4] = 1

                # Relay Port 3
                if(BuildSettings.FNC_List[i][2][1] == 2):
                    if(BuildSettings.FNC_List[i][3] == 4):
                        relayConfig[5] = 0
                    elif(BuildSettings.FNC_List[i][3] == 5):
                        relayConfig[5] = 1

                # Relay Port 2  
                if(BuildSettings.FNC_List[i][2][1] == 1):
                    if(BuildSettings.FNC_List[i][3] == 4):
                        relayConfig[6] = 0
                    elif(BuildSettings.FNC_List[i][3] == 5):
                        relayConfig[6] = 1

                # Relay Port 1
                if(BuildSettings.FNC_List[i][2][1] == 0):
                    if(BuildSettings.FNC_List[i][3] == 4):
                        relayConfig[7] = 0
                    elif(BuildSettings.FNC_List[i][3] == 5):
                        relayConfig[7] = 1

            # AC Relay Side 8-5
            elif(BuildSettings.FNC_List[i][2][0] == 4):
                print("PRIMARY AC RELAY")

                # Relay Ports 8/7
                if(BuildSettings.FNC_List[i][2][1] == 7 or BuildSettings.FNC_List[i][2][1] == 6):
                    if(BuildSettings.FNC_List[i][3] == 4):
                        relayConfig[0] = 0
                        relayConfig[1] = 0
                    elif(BuildSettings.FNC_List[i][3] == 5):
                        relayConfig[0] = 1
                        relayConfig[1] = 1

                # Relay Ports 6/5
                elif(BuildSettings.FNC_List[i][2][1] == 5 or BuildSettings.FNC_List[i][2][1] == 4):
                    if(BuildSettings.FNC_List[i][3] == 4):
                        relayConfig[2] = 0
                        relayConfig[3] = 0
                    elif(BuildSettings.FNC_List[i][3] == 5):
                        relayConfig[2] = 1
                        relayConfig[3] = 1
                
        functionSatisfied = False

    
def sensorRead():
    databaseString = ""
    print('Reading ADS1x15 values, press Ctrl-C to quit...')
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
    print('-' * 37)
    values = [0]*4

    # Combine both sensor arrays into one for simplified readings
    sensorActive = BuildSettings.PAP + BuildSettings.PDP
    print(sensorActive)

    # Run try loop while CTRL + C is not pressed
    try:
        i = 0
        print("STARTING READINGS - ")
        # Loop to read all 16 sensor values when active
        while(1):
            # 1 means the sensor is active
            if(sensorActive[i] == 1):
                print("SENSOR",i,"ON")

                # Check to see whether 3 or 5 volts are being used
                if(BuildSettings.PAV[i] == 3 or BuildSettings.PAV[i] == 5):
                    if(BuildSettings.PAV[i] == 3):
                        print("CHARGING 3 VOLTS")
                        GPIO.output(twoVoltageSwitch, GPIO.HIGH)
                    elif(BuildSettings.PAV[i] == 5):
                        print("CHARGING 5 VOLTS")
                        GPIO.output(twoVoltageSwitch, GPIO.LOW)
                    time.sleep(1)

                    # Indices 0 - 7 are Analog
                    if(i < 8):
                        print("ANALOG")
                        # Turn on the corresponding sensor in the Analog 8 MUX
                        muxDeciderEightAnalog(i)
                        # Turn on the Analog path in the 2 MUX
                        GPIO.output(twoAnalogDigital, GPIO.HIGH)
                        # Turn on the corresponding resistor in the 16 MUX
                        muxDeciderSixteenResistors(BuildSettings.PAR[i])
                        time.sleep(1)
                        # Read sensor value from the ADC
                        for j in range(4):
                            values[j] = adc.read_adc(j, gain=GAIN)
                        print('VALUE -{1:>6}'.format(*values))
##                        print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
                        databaseString += str(values[1])       

                    # Indices 8 - 15 are Analog  
                    elif(i > 7):
                        print("DIGITAL")
                        # Turn on the corresponding sensor in the Digital 8 MUX
                        muxDeciderEightDigital(i - 8)
                        time.sleep(1)
                        # Read sensor value from the GPIO pin
                        databaseString += str(GPIO.input(twoPinDigitalRead))
                        print("VALUE - ",GPIO.input(twoPinDigitalRead))

             # 0 means the sensor is inactive
            else:
                print("SENSOR",i,"INACTIVE")
                databaseString += "0"
                
            if(i < 15):
                i += 1       
                databaseString += ","
                outputReset()
                time.sleep(.1)
            else:
                i = 0

                # Update sensor readings into format for database
                sensorResults = databaseString
                databaseString += ","
                databaseString += str(time.time() / 3600)
                databaseArray = {'dataarray' : databaseString}
                currentTime = int(time.time() - startTime)
                print("In sensor",currentTime)
                if((currentTime % 15) < 4):
                    print("SEND TO DATABASE")
##                    databaseSend(databaseArray)
                databaseString = ""

                print("")
                print(sensorResults)
                functionCheck(sensorResults)
                print("")

                # Update GPIO Extender values for relay and motors
                relaySend()
                motorControllerSend()
                
                outputReset()
                time.sleep(.1)

    # If CTRL + C is pressed, then reset outputs, cleanup GPIO, and turn off GPIO Extender
    except KeyboardInterrupt:
        outputReset()
        GPIO.cleanup()
        bus.write_byte_data(address, 0x02, 0xff)

sensorInitialization()
sensorRead()
