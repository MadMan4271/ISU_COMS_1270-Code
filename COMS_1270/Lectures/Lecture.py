#def evenOdd (x):
#    if x % 2 == 1:
#        print("odd")
#    else:
#        print("even")

# 2/12/2026

# Boolean operators
# AND, Or, and NOT
# Order of operations: NOT, AND, OR

# Order of operations
# Mathmatical operators (PEMDAS)
# Parentheses, Exponent, (Multiplication, Division), (Addition, Subtraction)
# Comparison operatiors: <, >, <=, >=, ==
# Boolean Operatiors: NOT, AND, OR
# Otherwise, left to right

# For Loops:
# Require several aspects to make it work:
# The first is the 'for' keyword
# The second is a loop variable
# The third is a 'collection of stuff'
# The fourth is a colon at the end
# For loops require something inside to work
# Ex:
# for i in ["Alice", "Bob", "Charlie", "Daniel"]:
#    print(f"Hello, {i}, it's a nice day today!) 

# Ctrl + / <-- Mass comment

# Example: 
# Write a function which takes a interger n as a parameter
# The function should sum all the numbers from 1 to n but only if they are divisible by 3
# Return the final sum value

def SumIfThree(n):
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            sum += i
    return sum

#   for i in range(3, n+1, 3):
#       if i <= n: 
#           sum += i
#

def main():
    n = int(input("Give number: "))
    print(SumIfThree(n))

if __name__ == "__main__":
    main()