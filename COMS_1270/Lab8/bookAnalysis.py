# Caden Burbridge       3/30/2026
# Lab 8 - This code analysis any .txt file via counting every time a word is used

import removeNonASCII

def analyzeBook(name):
    with open(f'{name}.txt', 'r') as file:
        count = {}
        for line in file:
            for word in line.split():
                # remove punctuation
                word = word.replace('_', '').replace('"', '').replace(',', '').replace('.', '')
                word = word.replace('-', '').replace('?', '').replace('!', '').replace("'", "")
                word = word.replace('(', '').replace(')', '').replace(':', '').replace('[', '')
                word = word.replace(']', '').replace(';', '')
            
                # ignore case
                word = word.lower()

                # ignore numbers
                if word.isalpha():
                    if word in count:
                        count[word] = count[word] + 1
                    else:
                        count[word] = 1
    return count

def outputAnalysis(name, count):
    keys = list(count.keys())
    keys.sort()
    # save the word count analysis to a file
    with open(f'{name}_words.txt', 'w') as out:
        for word in keys:
            out.write(word + " " + str(count[word]))
            out.write('\n')
    return out

def main():
    name = input("Please give the name of the .txt file: ")
    string = removeNonASCII.stringCall(name)
    string = removeNonASCII.removeNonASCII(string)
    count = analyzeBook(name)
    outputAnalysis(name,count)

if __name__ == "__main__":
    main()
