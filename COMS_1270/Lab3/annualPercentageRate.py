# Caden Burbridge                       02/09/2026
# Lab week 3 - This calculates apr

def annualPercentageRate(intc, fee, loan, days):
    return (((intc + fee) / loan) / days) *100

def main():
    ic = float(input("What are the interest charges in decimal form: "))

    f = float(input("What are the fees: "))

    la = float(input("What is the loan ammount: "))

    d = float(input("What are the number of days on in the loan term: "))

    # Citation - https://www.investopedia.com/terms/a/apr.asp, Jason Fernando, 12/19/2025 (2/2/2026)

    apr = annualPercentageRate(ic, f, la, d)

    print(f"Your apr is: {apr}")

if __name__ == "__main__":
    main()