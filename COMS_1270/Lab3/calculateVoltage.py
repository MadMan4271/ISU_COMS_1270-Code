# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates voltage

def calculateVoltage(cur, res):
    return res * cur

def main():
    c = float(input("What is the current: "))

    r = float(input("What is the resistance: "))

    # Citation - https://www.fluke.com/en-us/learn/blog/electrical/what-is-ohms-law (2/2/2026)

    v = calculateVoltage(c, r)

    print(f"The voltage is: {v}")

if __name__ == "__main__":
    main()