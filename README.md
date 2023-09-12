# **Engineering 4 Notebook**

&nbsp;

## **Table of Contents**
* [Launchpad](#launchpad)
    * [Part 1](#launchpad-part-1)
    * [Part 2](#launchpad-part-2)
    * [Part 3](#launchpad-part-3)
    * [Part 4](#launchpad-part-4)
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

Write your assignment description here. What is the purpose of this assignment? It should be at least a few sentences.

#### **Evidence**
#
<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.gif?raw=true" width="300">

#
#### **Wiring**

<img src="https://github.com/mcolvin35/Engineering_4_Notebook/blob/main/images/weirdfish.jpg?raw=true" width="300"> 

#### **Code**

<details>
<summary>Title</summary>

```python
    print("hello world!")
```
</details> 

#### **Reflection**

What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience? Your goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person. Think about your audience for this one, which may be "future you" (when you realize you need some of this code in three months), me, or your college admission committee!

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
