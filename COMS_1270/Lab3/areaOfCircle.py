# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates the area of a circle

import math

def areaOfCircle(rad):
    return pow(rad,2) * math.pi

def main():
    rad = float(input("What is the radius of the circle: "))

    # Citation - https://www.cuemath.com/geometry/area-of-a-circle/ (2/2/2026)

    area = areaOfCircle(rad)

    print(f"The area of the circle is: {area}")

if __name__ == "__main__":
    main()