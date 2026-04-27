# Caden Burbridge 2/25/2026
# Lab 5 - This file creates a right triangle out of stars with a given input side length

def starRightTriangle(num):
    tri = ""
    for i in range(1, num+1):
        tri += "*"
        print(tri)

def main():
    integer = int(input("Please give an integer for the side length of the triangle"))
    starRightTriangle(integer)

if __name__ == "__main__":
    main()