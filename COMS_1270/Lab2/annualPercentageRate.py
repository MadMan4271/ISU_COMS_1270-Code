ic = float(input("What are the interest charges in decimal form: "))

f = float(input("What are the fees: "))

la = float(input("What is the loan ammount: "))

d = float(input("What are the number of days on in the loan term: "))

#Citation - https://www.investopedia.com/terms/a/apr.asp, Jason Fernando, 12/19/2025 (2/2/2026)

apr = (((ic+f) / la) / d) * 100

print("Your apr is: " + str(apr))