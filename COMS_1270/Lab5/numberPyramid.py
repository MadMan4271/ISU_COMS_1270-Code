# Caden Burbridge 2/26/2026
# Lab 5 - This file creates a pyramid out of numbers which increase from left to right

def numberPyramid(num):
    for i in range(1, num+1):
        string = ""
        string += " " * (num - i)
        for j in range(1, i + 1):
            string += f" {j}"
        print(string)
        

def main():
    num = int(input("Please give the base length of the pyramid: "))
    numberPyramid(num)

if __name__ == "__main__":
    main()