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

sensorPin3 = 21
sensorPin5 = 20
#tempSensor = 16
S0 = 19
S1 = 26
S2 = 12
S3 = 16

GPIO.setup(sensorPin3, GPIO.OUT)
GPIO.setup(sensorPin5, GPIO.OUT)

GPIO.setup(S0, GPIO.OUT)
GPIO.setup(S1, GPIO.OUT)
GPIO.setup(S2, GPIO.OUT)
GPIO.setup(S3, GPIO.OUT)

#GPIO.setup(tempSensor, GPIO.IN, GPIO.PUD_DOWN)

GPIO.output(sensorPin3, GPIO.LOW)
GPIO.output(sensorPin5, GPIO.LOW)

try:
    while(1):
        GPIO.output(S0, GPIO.LOW)
        GPIO.output(S1, GPIO.LOW)
        GPIO.output(S2, GPIO.HIGH)
        GPIO.output(S3, GPIO.LOW)

        GPIO.output(sensorPin5, GPIO.HIGH)
        GPIO.output(sensorPin3, GPIO.LOW)

        print(mcp.read_adc(0))
    
    while(1):
        GPIO.output(sensorPin5, GPIO.HIGH)
        GPIO.output(sensorPin3, GPIO.LOW)
        print("5 VOLTS")
        print(mcp.read_adc(0))
        time.sleep(2)

        print("ZERO")
        GPIO.output(sensorPin5, GPIO.LOW)
        GPIO.output(sensorPin3, GPIO.LOW)
        print(mcp.read_adc(0))
        time.sleep(3)
        
        GPIO.output(sensorPin3, GPIO.HIGH)
        GPIO.output(sensorPin5, GPIO.LOW)
        print("3 VOLTS")
        print(mcp.read_adc(0))
        time.sleep(2)

        print("ZERO")
        GPIO.output(sensorPin5, GPIO.LOW)
        GPIO.output(sensorPin3, GPIO.LOW)
        print(mcp.read_adc(0))
        time.sleep(3)

except KeyboardInterrupt:
    GPIO.output(sensorPin3, GPIO.LOW)
    GPIO.output(sensorPin5, GPIO.LOW)
    GPIO.cleanup()
