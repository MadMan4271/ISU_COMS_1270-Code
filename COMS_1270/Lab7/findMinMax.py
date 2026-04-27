# Caden Burbridge       3/29/2026
# Lab 7 - This code finds the minimum and maximum value in an inputed list of strings

def listInput():
    lis = []
    while True:
        add = input("Please give a number to add to the list, input * to stop: ")
        if add == "*":
            break
        elif ():
            pass
        else: 
            lis += add
    return lis

def convertList(lis):
    newLis = lis
    for i in range(len(lis)):
        newLis[i] = int(lis[i])
    return newLis

def findMax(lis):
    Max = 0
    for i in range(len(lis)):
        if i == 0:
            Max = lis[i]
        else:
            if Max < lis[i]:
                Max = lis[i]
    return Max


def findMin(lis):
    Min = 0
    for i in range(len(lis)):
        if i == 0:
            Min = lis[i]
        else:
            if Min > lis[i]:
                Min = lis[i]
    return Min

def main():
    lis = listInput()
    lis = convertList(lis)
    print(f"Max: {findMax(lis)}")
    print(f"Min: {findMin(lis)}")

if __name__ == "__main__":
    main()