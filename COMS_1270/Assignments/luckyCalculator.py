# Caden Burbridge           2/20/2026
# Assignment #2

# This calculator does the 7 basic functions 
# of a calculator and can generate a lucky number.

import random

def main():
    q = True
    while q :
        print("Luck Calculator", "\n"
        "By: Caden Burbridge", "\n"
        "[COMS 1270 C]", "\n" \
        "c - Calculator", "\n"
        "l - Lucky number","\n"
        "q - Quit")
        calTy = input("Please select one of the options:")
        if calTy == "c":
            print("+ - Addition" \
            "\n - - Subtraction" \
            "\n * - Multiplication" \
            "\n / - Division" \
            "\n // - Floor Division" \
            "\n % - Mod" \
            "\n ** - Exponent")
            funTy = input("Please select a function to use:")
            if funTy == "+":
                i1 = int(input("Please give an integer:"))
                i2 = int(input("Please give an integer:"))
                calc = i1 + i2
                print(f"The result of the calculation is {calc}")
            elif funTy == "-":
                i1 = int(input("Please give an integer:"))
                i2 = int(input("Please give an integer:"))
                calc = i1 - i2
                print(f"The result of the calculation is {calc}")
            elif funTy == "*":
                i1 = int(input("Please give an integer:"))
                i2 = int(input("Please give an integer:"))
                calc = i1 * i2
                print(f"The result of the calculation is {calc}")
            elif funTy == "/":
                i1 = int(input("Please give an integer:"))
                i2 = int(input("Please give an integer:"))
                if i2 == 0:
                    print("ERROR cannot divide by 0")
                    q = False
                else:
                    calc = i1 / i2
                    print(f"The result of the calculation is {calc}")
            elif funTy == "//":
                i1 = int(input("Please give an integer:"))
                i2 = int(input("Please give an integer:"))
                if i2 == 0:
                    print("ERROR cannot divide by 0")
                    q = False
                else:
                    calc = i1 // i2
                    print(f"The result of the calculation is {calc}")
            elif funTy == "%":
                i1 = int(input("Please give an integer:"))
                i2 = int(input("Please give an integer:"))
                if i2 == 0:
                    print("ERROR cannot compute mod 0")
                    q = False
                else:
                    calc = i1 % i2
                    print(f"The result of the calculation is {calc}")
            elif funTy == "**":
                i1 = int(input("Please give an integer:"))
                e1 = int(input("Please give an exponent:"))
                calc = i1 ** e1
                print(f"The result of the calculation is {calc}")
        elif calTy == "l":
            i1 = int(input("Please give an integer:"))
            i2 = int(input("Please give an integer:"))
            calc = random.randrange(i1, i2)
            print(f"The lucky number is {calc}")
        elif calTy == "q":
            q = False

if __name__ == "__main__":
    main()