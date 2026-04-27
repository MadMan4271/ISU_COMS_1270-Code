# Caden Burbridge 02/16/2026
# Lab week 4 - This file determinds if a given year is a leap year

def findLeapYear(yr):
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else: 
        return False

def main():
    year = findLeapYear(int(input("Please give a year to see if its a leap year:")))
    if year :
        print("The year you gave is a leap year")
    else:
        print("The year you gave is not a leap year")

if __name__ == "__main__":
    main()