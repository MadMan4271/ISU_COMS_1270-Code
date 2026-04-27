# Caden Burbridge 2/26/2026
# Lab 5 - This file creates a diamond out of numbers which increase from left to right and then decrease

def numberDiamond(num):
    lt = []
    for i in range(1, num+1):
        lt += ' '
    for i in range(1, num + 1):
        string = ""
        string += " " * (num - i)
        for j in range(1, i + 1):
            string += f" {j}"
        lt[i-1] = string
    for i in range(0, (len(lt)*2) - 1):
        if i < (len(lt) - 1):
            print(lt[i])
        else:
            print(lt[(len(lt) - 1) - ((i+1) % len(lt))])        

def main():
    num = int(input("Please give the width of the diamond: "))
    numberDiamond(num)

if __name__ == "__main__":
    main()