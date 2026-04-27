# Caden Burbridge 02/16/2026
# Lab week 4 - This file has tests the imported functions

import myShapes

import myFinances

import myPhysics

import myOhmsLaw

def main():
    bol = True
    while bol:
        print("s - Shape functions", "\n"
        "f - Finance functions", "\n"
        "p - Physics functions", "\n"
        "o - Ohms law functions", "\n"
        "q - Quit the program")
        funcTy = input("Please select the function catagory you want: ")
        if funcTy == "s":
            print("1 - Area of a circle function", "\n"
            "2 - Area of a rectangle function", "\n"
            "3 - Circumference of a circle function", "\n"
            "4 - Perimeter of a rectangle function")
            sTy = input("Please select what function you would like to use: ")
            if sTy == "1":
                r = float(input("Please give a radius for your circle: "))
                print(f"The area of the circle is {myShapes.areaOfCircle(r)}")
            elif sTy == "2":
                base = float(input("Please give the base for your rectangle: "))
                height = float(input("Please give the height for your rectangle: "))
                print(f"The area of the rectangle is {myShapes.areaOfRectangle(base,height)}")
            elif sTy == "3":
                r = float(input("Please give a radius for your circle: "))
                print(f"The circumference of the circle is {myShapes.circleCircumference(r)}")
            elif sTy == "4":
                base = float(input("Please give the base for your rectangle: "))
                height = float(input("Please give the height for your rectangle: "))
                print(f"The perimeter of the rectangle is {myShapes.rectanglePerimeter(base,height)}")
            else:
                print("Invalid Inputs")
        elif funcTy == "f":
            print("1 - Annual percentage rate function", "\n"
                  "2 - Compound ammount function")
            fTy = input("Please select what function you would like to use: ")
            if fTy == "1":
                ic = float(input("What are the interest charges in decimal form: "))
                f = float(input("What are the fees: "))
                la = float(input("What is the loan ammount: "))
                d = float(input("What are the number of days on in the loan term: "))
                apr = myFinances.annualPercentageRate(ic, f, la, d)
                print(f"Your apr is: {apr}")
            elif fTy == "2":
                    p = float(input("What is the principle amount: "))
                    r = float(input("What is the interest rate in percentage form: "))
                    c = float(input("How any times per year does the interest compound: "))
                    aa = myFinances.compoundAmount(p, r, c)
                    print(f"Your accrued interest is: {aa}")
        elif funcTy == "p":
            print("1 - Distance using speed and time function", "\n"
                  "2 - Velocity using initial velocity, acceleration and time function")
            pTy = input("Please select what function you would like to use: ")
            if pTy == "1":
                v = float(input("What is the speed in meters per second: "))
                t = float(input("What is the time in seconds: "))
                distance = myPhysics.distanceSpeedTime(v, t)
                print(f"The total distance traveled is: {distance}")
            if pTy == "2":
                t = float(input("What is the time in seconds: "))
                v = float(input("What is the initial velocity in meters per second: "))
                a = float(input("What is the acceleration in meter per second squared: "))
                vf = myPhysics.velocityAccelerationTime(t, v, a)
                print(f"The final velocity is: {vf}")    
        elif funcTy == "o":
            print("1 - Current calculation function", "\n"
                  "2 - Resistance calculation function", "\n"
                  "3 - Voltage calculation function")
            oTy = input("Please select what function you would like to use: ")
            if oTy == "1":
                r = float(input("What is the resistance: "))
                v = float(input("What is the voltage: "))
                c = myOhmsLaw.calculateCurrent(r, v)
                print(f"The current is: {c}")
            if oTy == "2":
                c = float(input("What is the current: "))
                v = float(input("What is the voltage: "))
                r = myOhmsLaw.calculateResistance(c, v)
                print(f"The resistance is: {r}")
            if oTy == "3":
                c = float(input("What is the current: "))
                r = float(input("What is the resistance: "))
                v = myOhmsLaw.calculateVoltage(c, r)
                print(f"The voltage is: {v}")
        elif funcTy == "q":
            bol = False
        else:
            print("Invalid Inputs")


if __name__ == "__main__":
    main()