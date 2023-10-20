# **Engineering 4 Notebook**

&nbsp;

## **Table of Contents**
* [Launchpad](#launchpad)
    * [Part 1](#countdown)
    * [Part 2](#lights)
    * [Part 3](#button)
    * [Part 4](#servo)
* [Crash Avoidance](#crash-avoidance)
    * [Part 1](#accelerometer)
    * [Part 2](#lightpower)
    * [Part 3](#oled-screen)
* [FEA Beam](#fea-beam)
    * [Part 1](#fea-beam)
    * [Part 3](#fea-analysis)
    * [Part 4](#iterative-design)
    * [Part 5](#final-beam)
&nbsp;

## **Launchpad**
#
## **Countdown**
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
## **Lights**
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
## **Button**
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
## **Servo**
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
## **Accelerometer**
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
## **Light+Power**
#
#### **Description**
Make the board run unplugged from a computer, and make a warning light turn on when it's on its side

#### **Evidence**
#
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/crash_p2.gif?raw=true" width="400">

#
#### **Wiring**
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/crash_p2_diagram.png?raw=true" width="400">  

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

#
## **OLED Screen**
#
#### **Description**
Make an OLED screen display angular velocity values to 3 decimal places

#### **Evidence**
#
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/crash_p3.gif?raw=true" width="400">

#
#### **Wiring**
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/crash_p3_diagram.png?raw=true" width="300">  

####

 **Code**
<details>
<summary>Crash Avoidance Part 3 Code</summary>

```python
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

sda_pin = (board.GP26) #set SDA as GP26 and SCL as GP27
scl_pin = (board.GP27)

i2c = busio.I2C(scl_pin, sda_pin) #setup I2C connection
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68) #setup accelerometer 

display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP17)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

led=digitalio.DigitalInOut(board.GP16) #assign LED to GP16 and set it as output
led.direction=digitalio.Direction.OUTPUT 

while True:
    splash = displayio.Group() #create display group

    title = "ANGULAR VELOCITY"

    header = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=18, y=10) #setup location for all lines
    X_display = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=45, y=25)
    Y_display = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=45, y=40)
    Z_display = label.Label(terminalio.FONT, text=title, color=0xFFFF00, x=45, y=55)
    splash.append(header)
    splash.append(X_display)    
    splash.append(Y_display) 
    splash.append(Z_display) 

    header = "ANGULAR VELOCITY:" #print header and all gyro values
    X_display.text = f"X:{round(mpu.gyro[0], 3)}" 
    Y_display.text = f"Y:{round(mpu.gyro[1], 3)}"
    Z_display.text = f"Z:{round(mpu.gyro[2], 3)}"

    display.show(splash) #send display group to screen

    time.sleep(0.2) #wait so the values are readable
    if mpu.acceleration[2] < 1 and mpu.acceleration[2] > -12: #if z acceleration is less than 1 (meaning board is on its side) and greater than -12 (so LED won't turn on when board is accelerating in Z)
        if mpu.acceleration[0] > +-5 or mpu.acceleration[1] > +-5: #also, if X and Y acceleration are greater than positive or negative 5 (meaning gravity is affecting one of them)
            led.value=True #turn LED on
    else: #otherwise
        led.value=False #LED is off
```
</details>

#### **Reflection**
My biggest hurdle for this assignment was figuring out how to code for the OLED screen. You need to create a display group, define everything in that group, and then send it to the screen. 

&nbsp;

#
## **FEA Beam**
#
## **First Design**

### Assignment Description
For this assignment we needed to design a beam to hold the most weight possible. The beam fails if it either bends over 35 mm or breaks. The requirements are as follows.
* The beam must use the provided attachment block with no modifications.
* The beam with the attachment block must be able to fully engage with the holder
* The beam must use the example eye bolt mounting geometry
* The center of the eyebolt hole must be 180 mm from the front face of the attachment block (in a direction perpendicular to the front face)
* No part of the beam may extend below the bottom face of the attachment block
* All vertical angles must be >= 45° measured relative to the horizontal plane (no overhangs)
* The beam must be PLA material
* **The entire beam, including attachment block, must weigh <= 13 grams**
#

### Part Link

[Link to the Onshape document](https://cvilleschools.onshape.com/documents/5ca195b929dce9b9f5de0c38/w/484c080f78991bb9985dcd6a/e/202c4b844babd7b88e7d7022?renderMode=0&uiState=651ad471654b7d4777a38ffc).
#

### Part Image
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/fea1.png?raw=true" >

#

### Reflection
This assignment had a lot of challenges since the guidelines were very limiting. Not being able to have any overhangs was the tough part, but we were able to work around that by using ovals instead of triangles. 

#
## **FEA Analysis**

### Assignment Description
The task for this assignment was to use Onshape's FEA simulation to analyze our beam and predict how it would perform. 
#

### Part Link

[Link to the Onshape document](https://cvilleschools.onshape.com/documents/5ca195b929dce9b9f5de0c38/w/484c080f78991bb9985dcd6a/e/202c4b844babd7b88e7d7022?renderMode=0&uiState=651ad471654b7d4777a38ffc).
#

### Part Image
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/fea_v1sim.png?raw=true" >

#

### Reflection
There were a lot of sharp edges in this beam that seemed to be experiencing stress, so in the next version we tried to round off a lot of the edges and also moved more mass closer to the back part that was under high stress. 
#

## **Iterative Design**

### Assignment Description
The task for this assignment was to improve our beam based on what we found from the simulation.
#

### Part Link

[Link to the Onshape document](https://cvilleschools.onshape.com/documents/5ca195b929dce9b9f5de0c38/w/484c080f78991bb9985dcd6a/e/202c4b844babd7b88e7d7022?renderMode=0&uiState=651ad471654b7d4777a38ffc).
#

### Part Image
<img src="https://github.com/dhalber11/Engineering_4_Notebook/blob/main/images/v2.png?raw=true" >

<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/fea_v2sim.png?raw=true" >

#

### Reflection
Sadly, this beam ending up being worse than our original design. It looks like there's less stress overall but that actual calculations shows that there's more stress. I think we might have removed too much mass from the middle part of the beam, and we should've kept it as a uniform beam.
#

## **Final Beam**
#

### Assignment Description
For this assignment we were supposed to use the knowledge we learned from the beam breaking in order to improve our beams.
#

### Part Link

[Link to the Onshape document](https://cvilleschools.onshape.com/documents/5ca195b929dce9b9f5de0c38/w/484c080f78991bb9985dcd6a/e/202c4b844babd7b88e7d7022?renderMode=0&uiState=651ad471654b7d4777a38ffc).
#

### Part Image
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/fea_v3.png?raw=true" >

<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/fea_v3sim.png?raw=true" >

#

### Reflection
After the original success of the I-beam based designs in the first round, we wanted to do something similar while still preserving our integrity. This beam was the result, a solid beam that tapers closer to the end with round edges. It was a **huge** improvement from the other versions. It deflected fairly easily, but it never broke and basically just became a rope.


&nbsp;

## **Media Test**

Your readme will have various images and gifs on it. Upload a test image and test gif to make sure you've got the process figured out. Pick whatever image and gif you want!

### **Test Link**

[Test Link](https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.gif)

### **Test Image**

<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.jpg?raw=true" width="300"> 

### **Test GIF**

![weirdfish](https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.gif)
