def find_area(x1y1, x2y2, x3y3): 
    try: #if there is an error inside the loop, program won't close
        x1y1 = x1y1.split(",") #split x1y1 into 2 separate values at the comma
        x2y2 = x2y2.split(",")
        x3y3 = x3y3.split(",")
        
        x1 = float(x1y1[0]) #x1 is the first part 
        y1 = float(x1y1[1])
        x2 = float(x2y2[0])
        y2 = float(x2y2[1])
        x3 = float(x3y3[0])
        y3 = float(x3y3[1])

        area = (1/2)*abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)) #function for calculating area
        
        if area == 0: #if points don't make a triangle
            print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!") #print error message
        return area
    except: #if there is a syntax error
        print("These points are not a valid triangle. Please try again, and make sure you are using the x,y syntax!") #print error message

        area = 0
        return area

while True: 
    val1 = input("Enter first coordinate:")
    val2 = input("Enter second coordinate:")
    val3 = input("Enter third coordinate:")

    area = find_area(val1, val2, val3) #call function

    if area == 0:   
        continue
    
    else: #if everything works out
        print(f"The area of the triangle with vertices ({val1}), ({val2}), ({val3}) is {area} square km.") #print values