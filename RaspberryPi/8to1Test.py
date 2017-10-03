import RPi.GPIO as GPIO
import time
# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

sensorPinSelectA = 5
sensorPinSelectB = 6
sensorPinSelectC = 13
sensorOutput = 27

GPIO.setup(sensorPinSelectA, GPIO.OUT)
GPIO.setup(sensorPinSelectB, GPIO.OUT)
GPIO.setup(sensorPinSelectC, GPIO.OUT)
GPIO.setup(sensorOutput, GPIO.IN, GPIO.PUD_DOWN)

GPIO.output(sensorPinSelectA, GPIO.LOW)
GPIO.output(sensorPinSelectB, GPIO.LOW)
GPIO.output(sensorPinSelectC, GPIO.LOW)

try:
    while(1):
##        print("6")
##        GPIO.output(sensorPinSelectA, GPIO.LOW)
##        GPIO.output(sensorPinSelectB, GPIO.HIGH)
##        GPIO.output(sensorPinSelectC, GPIO.HIGH)
##        print(mcp.read_adc(1))
##        time.sleep(5)
        print("4")
        GPIO.output(sensorPinSelectA, GPIO.LOW)
        GPIO.output(sensorPinSelectB, GPIO.LOW)
        GPIO.output(sensorPinSelectC, GPIO.HIGH)
        print(mcp.read_adc(7))
        time.sleep(1)
        

except KeyboardInterrupt:
    GPIO.output(sensorPinSelectA, GPIO.LOW)
    GPIO.output(sensorPinSelectB, GPIO.LOW)
    GPIO.output(sensorPinSelectC, GPIO.LOW)
    GPIO.cleanup()
