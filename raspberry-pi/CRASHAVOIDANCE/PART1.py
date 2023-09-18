#type: ignore

import busio
import adafruit_mpu6050
import board
import time

sda_pin = (board.GP26)
scl_pin = (board.GP27)
i2c = busio.I2C(scl_pin, sda_pin)

mpu = adafruit_mpu6050.MPU6050(i2c)
accel = mpu.acceleration
gyro = mpu.gyro


while True:
    print(accel)

