#type: ignore

from adafruit_display_text import label
import board
import adafruit_displayio_ssd1306
import terminalio
import displayio
from adafruit_display_shapes.triangle import Triangle
from adafruit_display_shapes.line import Line
from adafruit_display_shapes.circle import Circle
import busio

displayio.release_displays() #setup for OLED display
sda_pin = board.GP26
scl_pin = board.GP27
i2c = busio.I2C(scl_pin, sda_pin)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3d, reset=board.GP28)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

base = displayio.Group() #create base display group
circle = Circle(64, 32, 3, outline=0xFFFF00) #plot circle to represent base
xline = Line(0, 32, 128, 32, color=0xFFFF00) #line for x-axis
yline = Line(64, 0, 64, 64, color=0xFFFF00) #y-axis
base.append(xline) #add shapes to base display group
base.append(yline)
base.append(circle)   
display.show(base) #display base display group

def find_area(x1y1, x2y2, x3y3): #define function
    try: #if there is an error inside try loop, program won't close
        x1y1 = x1y1.split(",") #split x1y1 into 2 separate values at the comma
        x2y2 = x2y2.split(",")
        x3y3 = x3y3.split(",")
        
        x1 = float(x1y1[0]) #x1 is the first value of x1y1
        y1 = float(x1y1[1]) #y1 is the second value of x1y1
        x2 = float(x2y2[0])
        y2 = float(x2y2[1])
        x3 = float(x3y3[0])
        y3 = float(x3y3[1])

        area = (1/2)*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)) #function for finding area of a triangle from points 
        
        if area == 0: #if points don't make a triangle
            print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!") #print error message
        return area
    except: #if there is a syntax error
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!") #print error message

        area = 0
        return area

while True: 
    val1 = input("Enter first coordinate:") #ask for first coordinate
    val2 = input("Enter second coordinate:")
    val3 = input("Enter third coordinate:")

    x1y1 = val1.split(",") #same stuff as before to get values outside the function
    x2y2 = val2.split(",")
    x3y3 = val3.split(",")
        
    x1 = float(x1y1[0])
    y1 = float(x1y1[1])
    x2 = float(x2y2[0])
    y2 = float(x2y2[1])
    x3 = float(x3y3[0])
    y3 = float(x3y3[1])

    area = find_area(val1, val2, val3) #call function

    if area == 0:
        continue
    
    else: #if everything works out 
        print(f"The area of the triangle with vertices ({val1}), ({val2}), ({val3}) is {area} square km.") #print message with values

        plot = displayio.Group() #create plot display group
        triangle = Triangle(int(x1+64), int(-y1+32), int(x2+64), int(-y2+32), int(x3+64), int(-y3+32), outline=0xFFFF00) #plot a triangle with values
        circle = Circle(64, 32, 3, outline=0xFFFF00) #same stuff as before so triangle won't clear everything else
        xline = Line(0, 32, 128, 32, color=0xFFFF00)
        yline = Line(64, 0, 64, 64, color=0xFFFF00)
        text = f"{area} km^2" #create text display
        area_display = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=26, y=8) #display text
        plot.append(area_display) #add text to display group
        plot.append(xline)
        plot.append(yline)
        plot.append(circle)   
        plot.append(triangle)
        display.show(plot) #display plot display group

        