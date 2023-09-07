#type: ignore

import time 
import board
import digitalio

red=digitalio.DigitalInOut(board.GP16) #assign red LED to pin 16 and set it as output 
red.direction=digitalio.Direction.OUTPUT 

green=digitalio.DigitalInOut(board.GP18) #assign green LED to pin 18 and set it as output 
green.direction=digitalio.Direction.OUTPUT

for x in range(10, 0, -1): #loop 10 times, counting down x each time 
    print(x) #print x 
    red.value=True #red LED on 
    time.sleep(0.5) #wait half a second
    red.value=False #red LED off
    time.sleep(0.5)
print("Liftoff!") #after 10 loops, print "Liftoff!"
green.value=True #green LED on 
time.sleep(10) #wait 10 seconds