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

sensorPinSelectA = 27
sensorPinSelectB = 22

GPIO.setup(sensorPinSelectA, GPIO.OUT)
GPIO.setup(sensorPinSelectB, GPIO.OUT)

try:
    while(1):
        print("HIGH")
        GPIO.output(sensorPinSelectA, GPIO.HIGH)
        GPIO.output(sensorPinSelectB, GPIO.LOW)
        time.sleep(5)
        print("LOW")
        GPIO.output(sensorPinSelectA, GPIO.LOW)
        GPIO.output(sensorPinSelectB, GPIO.HIGH)
        time.sleep(5)
        

except KeyboardInterrupt:
    GPIO.output(sensorPinSelectA, GPIO.LOW)
    GPIO.output(sensorPinSelectB, GPIO.LOW)
    GPIO.cleanup()
