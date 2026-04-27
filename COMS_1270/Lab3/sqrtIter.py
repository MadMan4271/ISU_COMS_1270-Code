# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates the square root of a number

# Citation - https://www.cuemath.com/algebra/square-root-of-2/ (02/09/2026)

def sqrtIter(x, iterations):
    guess = (x + 1) / 2
    for i in range(iterations):
        guess = ((x / guess) + guess) / 2
    return guess

def main():
    x = float(input("What is the number you want to square root: "))
    iterations = int(input("How many times do you want the square root to be calculated: "))

    answer = sqrtIter(x, iterations)
    print(f"The square root is: {answer}")

if __name__ == "__main__":
    main()