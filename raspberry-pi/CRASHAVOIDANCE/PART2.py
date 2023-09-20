#type: ignore

import busio
import adafruit_mpu6050
import board
import time
import digitalio

sda_pin = (board.GP26) #set SDA as GP26 and SCL as GP27
scl_pin = (board.GP27)
i2c = busio.I2C(scl_pin, sda_pin) #setup I2C connection

led=digitalio.DigitalInOut(board.GP16)
led.direction=digitalio.Direction.OUTPUT 

mpu = adafruit_mpu6050.MPU6050(i2c) #setup accelerometer 

while True:
    print(f"X:{mpu.acceleration[0]} Y:{mpu.acceleration[1]} Z:{mpu.acceleration[2]}") #print values
    time.sleep(0.2) #wait so the values are readable
    if mpu.acceleration[2] < 1 and mpu.acceleration[2] > -12:
        if mpu.acceleration[0] > +-5 or mpu.acceleration[1] > +-5:
            led.value=True
    else:
        led.value=False


    