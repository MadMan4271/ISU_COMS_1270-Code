# Caden Burbridge 3/6/2026
# COMS 1270 Assignment 3 - This file plays a game with usage of the random module via a computer opponent

import random

def main():
    print("Nimgrab")
    print("By Caden Burbridge")
    print("[COMS 1270 1]")
    menu = ""
    while True: 
        print("p - Play Nimgrab" \
        "\nr - Read the rules of Nimgrab" \
        "\nq - Quit the program")
        menu = input("Please select the option you would like to do: ")
        if ((menu == "p") or (menu == "q")) or (menu == "r"):
            break
    if menu == "p":
        p2 = ""
        while True:
            print("h - Play against a human" \
            "\nc - Play against a computer")
            p2 = input("Please select the option you would like to do: ")
            if (p2 == "h") or (p2 == "c"):
                break
            else:
                print("Invalid input please try again")
        if p2 == "c":
            item = 20
            while True:
                print(f"Items left: {item}")
                print("| " * item)
                take = ""
                while True:
                    take = int(input("Please give an amount you would like to take [1-3]: "))
                    if (take < 4) and (take > 0):
                        break
                    else:
                        print("Invalid input please try again")
                item -= take
                if item <= 0:
                    print("Player 1 took the last item, Computer wins")
                    break
                if item > 3:
                    take = random.randint(1,3)
                elif item == 3:
                    take = random.randint(1,2)
                elif item <= 2:
                    take = 1
                item -= take
                print(f"Computer takes: {take}")
                if item == 0:
                    print("Computer took the last item, Player 1 wins")
                    break
        else:
            item = 20
            while True:
                print(f"Items left: {item}")
                print("| " * item)
                take = ""
                print("Player 1 Turn")
                while True:
                    take = int(input("Please give an amount you would like to take [1-3]: "))
                    if (take < 4) and (take > 0):
                        break
                    else:
                        print("Invalid input please try again")
                item -= take
                if item <= 0:
                    print("Player 1 took the last item, Player 2 wins")
                    break
                print("Player 2 Turn")
                while True:
                    take = int(input("Please give an amount you would like to take [1-3]: "))
                    if (take < 4) and (take > 0):
                        break
                    else:
                        print("Invalid input please try again")
                item -= take
                if item <= 0:
                    print("Player 2 took the last item, Player 1 wins")
                    break
    elif menu == "r":
        print("This is Nimgrab, a game where you can play either against another person or a computer"
        "\nHere are the rules, you must each round choose an amount you want to take from the amount of items which always start at twenty"
        "\nThe amount you take must be between 1-3 and if you are the person to make the number of items = zero, then you lose!")
    else:
        print("Quitting Nimgrab")
    
    
    
    

if __name__ == "__main__":
    main()



