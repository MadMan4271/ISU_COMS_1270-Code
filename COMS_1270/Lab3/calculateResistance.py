# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates resistance

def calculateResistance(cur, volt):
    return volt/cur

def main():
    c = float(input("What is the current: "))

    v = float(input("What is the voltage: "))

    # Citation - https://www.fluke.com/en-us/learn/blog/electrical/what-is-ohms-law (2/2/2026)

    r = calculateResistance(c, v)

    print(f"The resistance is: {r}")

if __name__ == "__main__":
    main()