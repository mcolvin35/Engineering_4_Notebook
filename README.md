# **Engineering 4 Notebook**

&nbsp;

## **Table of Contents**
* [Launchpad](#launchpad)
    * [Part 1](#launchpad-part-1)
    * [Part 2](#launchpad-part-2)
    * [Part 3](#launchpad-part-3)
    * [Part 4](#launchpad-part-4)
* [Crash Avoidance](#crash-avoidance)
    * [Part 1](##crash-avoidance-part-1)
    * [Part 2](##crash-avoidance-part-2)
    * [Part 3](##crash-avoidance-part-3)
    * [Part 4](##crash-avoidance-part-4)
* [Onshape_Assignment_Template](#onshape_assignment_template)

&nbsp;

## **Launchpad**
#
## **Launchpad Part 1**
#
#### **Description**
Make a countdown timer that counts down each second from 10 to 0, and says "Liftoff" at 0. Must be printed to serial monitor.

#### **Evidence**
#
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/launchpad_p1.gif?raw=true" width="300">

#

#### **Code**

<details>
<summary>Launchpad Part 1 Code</summary>

```python
import time 
for x in range(10, 0, -1): #loop 10 times, counting x down each time 
    print(x) #print x 
    time.sleep(1) #wait 1 second
print("Liftoff!") #after 10 loops, print "Liftoff!"
```
</details>

#### **Reflection**

The challenge for this assignment was using the range function, since I haven't used that until now. The function give in output that starts at the first number, ends at the second number, and increments using the third number. 

#
## **Launchpad Part 2**
#
#### **Description**

Make a red LED blink each time the timer counts down, and a green LED turn on at liftoff.

#### **Evidence**
#
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/launchpad_p2.gif?raw=true" width="300">

#
#### **Wiring**

<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/lpad_2_diagram.png?raw=true" width="300"> 

#### **Code**

<details>
<summary>Launchpad Part 2 Code</summary>

```python
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
```
</details>

#### **Reflection**

For me the hardest part of this assignment was the wiring. It's pretty simple but I kept messing it up by arranging things horizontally across the board, so things that weren't supposed to be connected were connected. 

#
## **Launchpad Part 3**
#
#### **Description**

Add a button that starts the countdown. 

#### **Evidence**
#
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/launchpad_p3.gif?raw=true" width="300">

#
#### **Wiring**

<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/lpad_3_diagram.png?raw=true" width="300">  

#### **Code**

<details>
<summary>Launchpad Part 3 Code</summary>

```python
#type: ignore

import time 
import board
import digitalio

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
        time.sleep(5) #wait 5 seconds
        green.value=False
        c=button.value #current is button value (debouncing)
    p=c #previous is current (debouncing)
```
</details> 

#### **Reflection**

Since the Raspberry Pi has internal pull up resistors, the wiring of the button actually becomes a lot simpler than with the other boards as long as you use pull up, which kind of threw me off a little bit since it's different than what I've been doing. 

#
## **Launchpad Part 4**
#
#### **Description**

Make a 180 servo move on liftoff

#### **Evidence**
#
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/launchpad_p4.gif?raw=true" width="300">

#
#### **Wiring**

<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/lpad_4_diagram.png?raw=true" width="300"> 

#### **Code**

<details>
<summary>Title</summary>

```python
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
```
</details> 

#### **Reflection**

I forgot which wires were what on the servo. Yellow is signal, red is power, and brown is ground.

## **Crash Avoidance**
#
## **Crash Avoidance Part 1**
#
#### **Description**
Make an accelerometer print X, Y, and Z acceleration values 

#### **Evidence**
#
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/crash_p1.gif?raw=true" width="600">

#
#### **Wiring**
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/crash_p1_diagram.png?raw=true" width="300"> 

####

 **Code**
<details>
<summary>Crash Avoidance Part 1</summary>

```python
#type: ignore

import busio
import adafruit_mpu6050
import board
import time

sda_pin = (board.GP26) #set SDA as GP26 and SCL as GP27
scl_pin = (board.GP27)
i2c = busio.I2C(scl_pin, sda_pin) #setup I2C connection

mpu = adafruit_mpu6050.MPU6050(i2c) #setup accelerometer 

while True:
    print(f"X:{mpu.acceleration[0]} Y:{mpu.acceleration[1]} Z:{mpu.acceleration[2]}") #print values
    time.sleep(0.2) #wait so the values are readable
```
</details>

#### **Reflection**
This assignment went pretty smoothly. Most of what I needed to do was outlined in Canvas. One thing that confused me was why the Z acceleration constantly read around 10, and I learned that it's because the accelerometer accounts for the pull of gravity. 

#
## **Crash Avoidance Part 2**
#
#### **Description**
Make the board run unplugged from a computer, and make a warning light turn on when it's on its side

#### **Evidence**
#
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.gif?raw=true" width="300">

#
#### **Wiring**
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.jpg?raw=true" width="300">  

####

 **Code**
<details>
<summary>Crash Avoidance Part 2</summary>

```python
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

while True:
    print(f"X:{mpu.acceleration[0]} Y:{mpu.acceleration[1]} Z:{mpu.acceleration[2]}") #print values
    time.sleep(0.2) #wait so the values are readable
    if mpu.acceleration[2] < 1 and mpu.acceleration[2] > -12: #if z acceleration is less than 1 (meaning board is on its side) and greater than -12 (so LED won't turn on when board is accelerating in Z)
        if mpu.acceleration[0] > +-5 or mpu.acceleration[1] > +-5: #also, if X and Y acceleration are greater than positive or negative 5 (meaning gravity is affecting one of them)
            led.value=True #turn LED on
    else: #otherwise
        led.value=False #LED is off
```
</details>

#### **Reflection**
The hardest part of this assignment was getting everything to fit on one breadboard. There was just barely enough room in between the accelerometer and board for the battery to fit. 

&nbsp;

## Onshape_Assignment_Template

### Assignment Description

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

### Part Link 

[Create a link to your Onshape document](https://cvilleschools.onshape.com/documents/003e413cee57f7ccccaa15c2/w/ea71050bb283bf3bf088c96c/e/c85ae532263d3b551e1795d0?renderMode=0&uiState=62d9b9d7883c4f335ec42021). Don't forget to turn on link sharing in your Onshape document so that others can see it. 

### Part Image

Take a nice screenshot of your Onshape document. 

### Reflection

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

&nbsp;

## Media Test

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### Test Link

[Test Link](https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.gif)

### Test Image

<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.jpg?raw=true" width="300"> 

### Test GIF

![weirdfish](https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.gif)
