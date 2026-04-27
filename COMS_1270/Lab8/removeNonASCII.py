# Caden Burbridge       3/30/2026
# Lab 8 - This code cleans a text file to have only ASCII characters
#  encoding="utf-8" - currently utf-8
def stringCall(text):
    with open(f"{text}.txt", "r", encoding="utf-8") as file:
        call = file.read()
        return call
    
def removeNonASCII(string):
    clean = ""
    for i in range(0, len(string)):
        if ord(string[i]) <= 126:
            clean += string[i]
    return clean

def newTextFile(name,string):
    with open(f"{name}_clean.txt", "w") as file:
        file.write(string)


def main():
    name = input("Please give the name of the .txt file: ")
    string = stringCall(name)
    string = removeNonASCII(string)
    print(string)
    newTextFile(name,string)

if __name__ == "__main__":
    main()