#this program takes two points from the user and prints the line between those points
print("Enter two points and this program will compute the line connecting those points.")

try: #let's use example points (1,0) and (2,2)
    x1raw , y1raw = input("Please enter your first point in the following format: x,y  ").split(",") #user enters 1,0
    x2raw , y2raw = input("Please enter your second point in the following format: x,y  ").split(",") #user enters 2,2
    x1 = float(x1raw) #turns string from user into a float
    x2 = float(x2raw)
    y1 = float(y1raw)
    y2 = float(y2raw)

    m = float((y2 - y1) / (x2 - x1)) #calculates slope

    constant = y1 - m * x1 #this is to easily print the line in y=mx+b form

    print("Your line is: \ny = " + str(m) + "x" + " + " + str(constant)) #prints the equation in an eye-pleasing fashion
except ValueError:
    print("Please try again formatting your point(s) as 'x,y' using only numbers.") #user did not enter numbers properly or entered non-numeric characters