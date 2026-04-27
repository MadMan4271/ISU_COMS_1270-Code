import random

def randomProduct(a, b, c):
    product = 1
    for i in range(a):
        randomNum = random.randrange(b, c + 1)
        product *= randomNum

def main(): 
    a = int(input("Enter the number of random values you want to generate"))
    b = int(input("Enter the minimum number: "))
    c = int(input("Enter the maximum number: "))

    answer = randomProduct(a, b, c)

    print(f"The answer is: {answer}")

if __name__ == "__main__":
    main()