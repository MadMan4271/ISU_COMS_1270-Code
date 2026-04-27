# Caden Burbridge 2/25/2026
# Lab 5 - This file creates a multiplication table from a given lowest to a given highest number

def multiplicationTable(lowNum, highNum):
    for i in range(lowNum, highNum+1):
        string = " "
        header = " "
        if i == lowNum:
            for f in range(lowNum, highNum+1):
                if f == lowNum:
                    header += (f"   {f}").rjust(4) 
                else:
                    header += (f"{f}").rjust(4)
            print(header)
        for j in range(1, highNum+1):
                temp = f"{i*j}"
                string += (temp.rjust(4))
        print(string)

def main():
    low = int(input("Please give the lowest number in the multiplication table: "))
    high = int(input("Please give the highest number in the multiplaction table: "))
    multiplicationTable(low, high)

if __name__ == "__main__":
    main()