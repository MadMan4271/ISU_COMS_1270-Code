p = float(input("What is the principle amount: "))

r = float(input("What is the interest rate: "))

c = float(input("How any times per year does the interest compound: "))

# Citation - https://www.wallstreetprep.com/knowledge/accrued-interest/ (2/2/2026)

aa = p * (1 + (r/100) / c) ** c

print("Your accrued interest is: " + str(aa))