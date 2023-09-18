#type: ignore

import time 
import board
import digitalio
import pwmio
from adafruit_motor import servo

pwm_servo = pwmio.PWMOut(board.GP28, duty_cycle=2 ** 15, frequency=50) #assign servo to pin 28
serv = servo.Servo(pwm_servo, min_pulse=500, max_pulse=2500)


red=digitalio.DigitalInOut(board.GP16) #assign red LED to pin 16 and set it as output 
red.direction=digitalio.Direction.OUTPUT 

green=digitalio.DigitalInOut(board.GP18) #assign green LED to pin 18 and set it as output 
green.direction=digitalio.Direction.OUTPUT

button=digitalio.DigitalInOut(board.GP15) #assign button to pin 15 and set as input
button.direction=digitalio.Direction.INPUT 
button.pull=digitalio.Pull.UP #declare button as pull up, since rpi has built in pullup resistors

p=button.value #previous state is button value (debouncing)

while True:
    c=button.value #current state is button value (debouncing)
    if c != p and button.value == 0: #if current does not equal previous and button is pressed
        for x in range(10, 0, -1): #loop 10 times, counting down x each time 
            print(x) #print x 
            red.value=True #red LED on 
            time.sleep(0.5) #wait half a second
            red.value=False #red LED off
            time.sleep(0.5)
        print("Liftoff!") #after 10 loops, print "Liftoff!"
        green.value=True #green LED on 
        serv.angle=180 #move servo 180 degrees
        time.sleep(5) #wait 5 seconds
        green.value=False
        serv.angle=0 #move servo back
        c=button.value #current is button value (debouncing)
    p=c #previous is current (debouncing)