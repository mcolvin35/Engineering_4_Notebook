#type: ignore
#OLED: 0x3d
#MPU: 0x68

import busio
import adafruit_mpu6050
import board
import time
import digitalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio

displayio.release_displays()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP17)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)


sda_pin = (board.GP26) #set SDA as GP26 and SCL as GP27
scl_pin = (board.GP27)
i2c = busio.I2C(scl_pin, sda_pin) #setup I2C connection
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #setup accelerometer 

led=digitalio.DigitalInOut(board.GP16) #assign LED to GP16 and set it as output
led.direction=digitalio.Direction.OUTPUT 


splash = displayio.Group()

title = "ANGULAR VELOCITY"

text_area = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=5, y=5)
splash.append(text_area)    

display.show(splash)

while True:
    print(f"X:{mpu.acceleration[0]} Y:{mpu.acceleration[1]} Z:{mpu.acceleration[2]}") #print values
    text_area.text = f"{mpu.acceleration}"
    time.sleep(0.2) #wait so the values are readable
    if mpu.acceleration[2] < 1 and mpu.acceleration[2] > -12: #if z acceleration is less than 1 (meaning board is on its side) and greater than -12 (so LED won't turn on when board is accelerating in Z)
        if mpu.acceleration[0] > +-5 or mpu.acceleration[1] > +-5: #also, if X and Y acceleration are greater than positive or negative 5 (meaning gravity is affecting one of them)
            led.value=True #turn LED on
    else: #otherwise
        led.value=False #LED is off