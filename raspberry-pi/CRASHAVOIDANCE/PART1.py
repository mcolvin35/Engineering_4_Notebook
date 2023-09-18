#type: ignore

import busio
import adafruit_mpu6050
import board

sda_pin = board.31
scl_pin = board.32
i2c = busio.I2C(32, 31)

mpu = adafruit_mpu6050.MPU6050(i2c)
accel = mpu.acceleration
gyro = mpu.gyro


while True:
    print(accel)

