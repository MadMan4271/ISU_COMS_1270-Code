# Caden Burbridge       3/23/2026
# Lab 6 - This code finds if a given substring is within a given string

def findSubStringV1(sub,string):
    ret = string.find(sub)
    return ret

def findSubStringV2(sub,string):
    if sub in string:
        return string.index(sub)
    else:
        return -1

def findSubStringV3(sub,string):
    j = 0
    for i in range(0, len(string)):
        if len(sub) > len(string):
            return -1
        else:
            if string[i] == sub[j]:
                if j == 0:
                    start = i
                j += 1
                if j == len(sub):
                    return start
            else:
                j = 0
    return -1

def main():
    string = input("Give a string: ")
    sub = input("Give a string to check if its in the previously given string: ")
    print(findSubStringV1(sub,string))
    print(findSubStringV2(sub,string))
    print(findSubStringV3(sub,string))

if __name__ == "__main__":
    main()