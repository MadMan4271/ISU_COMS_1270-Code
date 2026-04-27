# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates the compounded amount

def compoundAmount(prin, rate, comp):
    return prin * (1 + (rate/100) / comp) ** comp


def main():
    p = float(input("What is the principle amount: "))

    r = float(input("What is the interest rate in percentage form: "))

    c = float(input("How any times per year does the interest compound: "))

    # Citation - https://www.wallstreetprep.com/knowledge/accrued-interest/ (2/2/2026)

    aa = compoundAmount(p, r, c)

    print(f"Your accrued interest is: {aa}")

if __name__ == "__main__":
    main()