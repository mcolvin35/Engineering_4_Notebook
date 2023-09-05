import time 
import board
import digitalio

led=digitalio.DigitalInOut(board.GP34)
led.direction=digitalio.Direction.OUTPUT

led.value=Trueprint("LED ON")