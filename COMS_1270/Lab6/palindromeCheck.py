# Caden Burbridge       3/23/2026
# Lab 6 - This code checks if an inputed string is a palindrome

import reverseString

def palindromeCheckV1(string):
    if string == reverseString.reverseStringV1(string):
        return True
    else:
        return False

def palindromeCheckV2(string):
    lis = list(string)
    for i in range(0,(len(lis)//2)):
        if i == ((len(lis)//2)+1):
            pass
        else:
            if lis[i] == lis[len(lis)-(1+i)]:
                pass
            else:
                return False
    return True


def main():
    string = input("Please give a string: ")
    print(palindromeCheckV1(string))
    print(palindromeCheckV2(string))
    

if __name__ == "__main__":
    main()