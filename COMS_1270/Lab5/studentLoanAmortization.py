# Caden Burbridge 2/23/2026
# Lab 5 - This file calculates the loan amortization of a student loan

def loanAmortization(prin,yir,yrs):
    np = yrs*12
    pb = prin
    interp = yir/12
    inter = (pb*yir)/(12)
    tpd = (pb*((interp*(1+interp)**np)/(((1+interp)**np)-1)))
    prind = tpd - inter
    print(f"Month" + 
              f"   Total Payment Due" + 
              f"   Interest Due" +
              f"        Principle Due" +
              f"       Principle Balance")
    for i in range(1,(yrs*12)+1):
        pb -= prind
        print(f"{i}" + 
              (" " * (8 - len(f"{i}")) +f"{tpd}") + 
              (" " * (20 - len(f"{tpd}")) +f"{inter}") +
              (" " * (20 - len(f"{inter}")) +f"{prind}") +
              (" " * (20 - len(f"{prind}")) +f"{pb}"))
        inter = (pb*yir)/(12)
        prind = tpd - inter
        
def main():
    # prin = float(input("Please enter the principle amount: "))
    # yir = float(input("Please enter the yearly interest rate: "))
    # yrs = int(input("Please enter the number of years the loan lasts: "))
    # loanAmortization(prin, yir, yrs)
    loanAmortization(30000, .05, 4)

if __name__ == "__main__":
    main()