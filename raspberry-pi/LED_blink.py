import board
import digitalio

led=digitalio.DigitalInOut(board.GP28)
led.direction=digitalio.Direction.OUTPUT

while True:
    led.value=True