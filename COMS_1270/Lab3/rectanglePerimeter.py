# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates the perimeter of a rectangle

def rectanglePerimeter(width, height):
    return 2 * width + 2* height

def main():
    width = float(input("What is the width of the rectangle: "))
    height = float(input("What is the height of the rectangle: "))
    
    # Citation - https://www.mometrix.com/academy/calculating-the-perimeter-of-rectangles/ (2/2/2026)

    peri = rectanglePerimeter(width, height)

    print(f"The perimeter of the rectangle is: {peri}")

if __name__ == "__main__":
    main()