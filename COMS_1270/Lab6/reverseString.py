# Caden Burbridge       3/2/2026
# Lab 6 - This code reverses an inputed string

def reverseStringV1(string):
    return string[::-1]

def reverseStringV2(string):
    lis = list(string)
    lis.reverse()
    ret = ""
    for i in range(0, len(string)):
        ret += lis[i]
    return ret

def reverseStringV3(string):
    ret = ""
    for i in range(-1, (-len(string))-1, -1):
        ret += string[i] 
    return ret

def reverseStringV4(string):
    ret = ""
    for letter in string:
        ret = letter + ret
    return ret

def reverseStringV5(string):
    ret = ""
    i = len(string)-1
    while True:
        ret = ret + string[i]
        if i == 0:
            break
        i -= 1
    return ret



def main():
    string = input("Please give some text you would like reversed: ")
    print(reverseStringV1(string))
    print(reverseStringV2(string))
    print(reverseStringV3(string))
    print(reverseStringV4(string))
    print(reverseStringV5(string))

if __name__ == "__main__":
    main()