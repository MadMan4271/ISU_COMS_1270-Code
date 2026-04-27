# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates the circumference of a circle

import math

def circleCircumference(rad):
    return 2 * rad * math.pi

def main():
    rad = float(input("What is the radius of the circle: "))

    # Citation - https://study.com/learn/lesson/circumference-cirlce-formula-area.html (2/2/2026)

    circum = circleCircumference(rad)

    print(f"The circumference of the circle is: {circum}")

if __name__ == "__main__":
    main()