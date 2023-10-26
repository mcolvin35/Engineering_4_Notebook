
def find_area(x1y1, x2y2, x3y3):
    try: 
        x1y1 = txt.split(", ")
        x2y2 = txt.split(", ")
        x3y3 = txt.split(", ")

        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        x3 = float(x3)
        y3 = float(y3)

        area = (1/2)|x1(y2-y3)+x2(y3-y1)+x3(y1-y2)|
        
        return area
    except: 
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!")

        area = 0
        return area

while True: 
    val1 = input("Enter first coordinate:")
    val2 = input("Enter second coordinate:")
    val3 = input("Enter third coordinate:")

    area = triangle_area(val1, val2, val3)

    if area == 0;
        Continue
    
    else: 
        print(f"The area of the triangle with vertices {val1}, {val2}, {val3} is {area} square km.")