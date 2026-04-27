# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates the area of a rectangle

def areaOfRectangle(base, height):
    return base * height

def main():
    base = float(input("What is the Base: "))

    height = float(input("What is the height: "))

    # Citation - https://www.cuemath.com/measurement/area-of-rectangle/ (2/2/2026)

    area = areaOfRectangle(base, height)

    print(f"The area is {area}")

if __name__ == "__main__":
    main()