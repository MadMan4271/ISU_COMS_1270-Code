# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates current

def calculateCurrent(res, volt):
    return res/volt

def main():
    r = float(input("What is the resistance: "))

    v = float(input("What is the voltage: "))

    # Citation - https://www.fluke.com/en-us/learn/blog/electrical/what-is-ohms-law (2/2/2026)

    c = calculateCurrent(r, v)

    print(f"The current is: {c}")

if __name__ == "__main__":
    main()