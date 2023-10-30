#type: ignore

from adafruit_display_text import label
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import busio

displayio.release_displays()
sda_pin = board.GP26
scl_pin = board.GP27
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, reset=board.GP28)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)


def find_area(x1y1, x2y2, x3y3):
    try: 
        x1y1 = x1y1.split(",")
        x2y2 = x2y2.split(",")
        x3y3 = x3y3.split(",")
        
        x1 = float(x1y1[0])
        y1 = float(x1y1[1])
        x2 = float(x2y2[0])
        y2 = float(x2y2[1])
        x3 = float(x3y3[0])
        y3 = float(x3y3[1])

        area = (1/2)*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
        
        if area == 0:
            print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!")
        return area
    except: 
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!")

        area = 0
        return area

while True: 
    val1 = input("Enter first coordinate:")
    val2 = input("Enter second coordinate:")
    val3 = input("Enter third coordinate:")

    area = find_area(val1, val2, val3)

    if area == 0:
        continue
    
    else: 
        print(f"The area of the triangle with vertices ({val1}), ({val2}), ({val3}) is {area} square km.")