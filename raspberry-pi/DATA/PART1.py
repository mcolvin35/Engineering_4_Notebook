#type: ignore

import busio
import adafruit_mpu6050
import board
import time
import digitalio

sda_pin = (board.GP26) #set SDA as GP26 and SCL as GP27
scl_pin = (board.GP27)
i2c = busio.I2C(scl_pin, sda_pin) #setup I2C connection

led=digitalio.DigitalInOut(board.GP16) #assign LED to GP16 and set it as output
led.direction=digitalio.Direction.OUTPUT 

mpu = adafruit_mpu6050.MPU6050(i2c) #setup accelerometer 

with open("/data.csv", "a") as datalog:
    datalog.write("=========,=========,=========,=========,=========\n") #write line to tell flights apart
    datalog.flush()
    while True:
        elapsed = time.monotonic()
        print(f"X:{mpu.acceleration[0]} Y:{mpu.acceleration[1]} Z:{mpu.acceleration[2]}") #print values
        time.sleep(0.2) #wait so the values are readable
        if mpu.acceleration[2] < 1 and mpu.acceleration[2] > -12: #if z acceleration is less than 1 (meaning board is on its side) and greater than -12 (so LED won't turn on when board is accelerating in Z)
            if mpu.acceleration[0] > +-5 or mpu.acceleration[1] > +-5: #also, if X and Y acceleration are greater than positive or negative 5 (meaning gravity is affecting one of them)
                led.value=True #turn LED on
                tilt = 1
        else: #otherwise
            led.value=False #LED is off
            tilt = 0
        datalog.write(f"{elapsed},{mpu.acceleration[0]},{mpu.acceleration[1]},{mpu.acceleration[2]},{tilt}\n") #write data to file 
        datalog.flush()