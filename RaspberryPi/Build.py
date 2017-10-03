from numpy import genfromtxt
import numpy as np
import RPi.GPIO as GPIO
import time
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensorPin3 = 22
sensorPin5 = 27
S0 = 26
S1 = 19
S2 = 21
S3 = 20

GPIO.setup(sensorPin3, GPIO.OUT)
GPIO.setup(sensorPin5, GPIO.OUT)

GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)

GPIO.output(sensorPin3, GPIO.LOW)
GPIO.output(sensorPin5, GPIO.LOW)

arraySize = 16
sensorActive = []
sensorType = []
sensorPin = []
sensorResistor = []
sensorVoltage = []
boolResult = []

def sensorFileSetup():
    global sensorActive
    global sensorType
    global sensorPin
    global sensorVoltage
    global sensorResistor
    data = genfromtxt("sensordata.txt", delimiter=",")

    #x = np.array(data[0])
    #x.astype(int)

    sensorActive = data[0] # 1 = ON
    sensorType = data[1] # 1 = ANALOG, 2 = DIGITAL, 3 = MISC
    sensorPin = data[2] # 2 PIN OR 3 PIN
    sensorVoltage = data[3] # 3 VOLTS OR 5 VOLTS
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
                
                if(sensorVoltage[i] == 3):
                    print("CHARGING 3 VOLTS")
                    GPIO.output(sensorPin3, GPIO.HIGH)
                    GPIO.output(sensorPin5, GPIO.LOW)
                    time.sleep(5)

                    if(sensorType[i] == 1):
                        print("ANALOG")

                        #3 PIN ANALOG DONE
                        if(sensorPin[i] == 3):
                            print("3 PIN")
                            muxDecider(i)
                            
                            time.sleep(1)
                            print("VALUE - ",mcp.read_adc(0))
                        #3 PIN ANALOG DONE
                            
                        elif(sensorPin[i] == 2):
                            print("2 PIN")
                            
                    elif(sensorType[i] == 2):
                        print("DIGITAL")
                        
                        if(sensorPin[i] == 3):
                            print("3 PIN")
                            
                        elif(sensorPin[i] == 2):
                            print("2 PIN")

                elif(sensorVoltage[i] == 5):
                    print("CHARGING 5 VOLTS")
                    GPIO.output(sensorPin5, GPIO.HIGH)
                    GPIO.output(sensorPin3, GPIO.LOW)
                    time.sleep(5)
                    
                    if(sensorType[i] == 1):
                        print("ANALOG")

                        #3 PIN ANALOG DONE
                        if(sensorPin[i] == 3):
                            print("3 PIN")
                            muxDecider(i)
                            
                            time.sleep(1)
                            print("VALUE - ",mcp.read_adc(0))
                        #3 PIN ANALOG DONE

                        elif(sensorPin[i] == 2):
                            print("2 PIN")
                            
                    elif(sensorType[i] == 2):
                        print("DIGITAL")
                        
                        if(sensorPin[i] == 3):
                            print("3 PIN")
                            
                        elif(sensorPin[i] == 2):
                            print("2 PIN")


            else:
                print("SENSOR",i,"INACTIVE")
                
            if(i < 4):
                i += 1
            else:
                i = 0

            GPIO.output(sensorPin5, GPIO.LOW)
            GPIO.output(sensorPin3, GPIO.LOW)
            GPIO.output(S0, GPIO.LOW)
            GPIO.output(S1, GPIO.LOW)
            GPIO.output(S2, GPIO.LOW)
            GPIO.output(S3, GPIO.LOW)
            time.sleep(1)
            

    except KeyboardInterrupt:
        GPIO.output(sensorPin3, GPIO.LOW)
        GPIO.output(sensorPin5, GPIO.LOW)
        GPIO.cleanup()


def muxDecider(i):
    binaryResult = format(i, "04b")
    #print(binaryResult[3])
    #print(binaryResult[2])
    #print(binaryResult[1])
    #print(binaryResult[0])
    #print(binaryResult)

    if(binaryResult[3] == '0'):
        GPIO.output(S0, GPIO.LOW)
    else:
        GPIO.output(S0, GPIO.HIGH)
        
    if(binaryResult[2] == '0'):
        GPIO.output(S1, GPIO.LOW)
    else:
        GPIO.output(S1, GPIO.HIGH)
        
    if(binaryResult[1] == '0'):
        GPIO.output(S2, GPIO.LOW)
    else:
        GPIO.output(S2, GPIO.HIGH)
        
    if(binaryResult[0] == '0'):
        GPIO.output(S3, GPIO.LOW)
    else:
        GPIO.output(S3, GPIO.HIGH)

            
sensorFileSetup()
sensorInitialization()
sensorRead()

#print(sensorActive)
