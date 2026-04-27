# Caden Burbridge 02/22/2026
# Lab week 4 - This file simulates a choose your own adventure story

def main():
    print("Adventure Story"
    "\n By Caden Burbridge" \
    "\n You find yourself placed in a small jail cell, there are a few things you can interact with inside the cell")

    c1 = input("Do you want to:"
    "\n 1 - Try to open the jail door"
    "\n 2 - Search around the room")
    while c1 == "1":
        print("You try to open the door and it doesn't budge")
        c1 = input("Do you want to"
        "\n 1 - Try to open the jail door"
        "\n 2 - Search around the room")
    if c1 == "2":
        print("You look under the bed in your cell and you find a hole that leads down underground"
        "\n You also find a poster on the wall")
        c2 = input("Do you want to:" \
        "\n 1 - Go down the hole under the bed" \
        "\n 2 - Check behind the poster")
        if c2 == "2":
            print("You look behind the poster and there is a brick wall so you had no other choice than to head into the tunnel")
            c2 = "1"
        if c2 == "1":
            print("You head into the tunnel and it leads further down and eventually leads back up to the inside of " \
            "a courtyard with a chainlink fence surrounding it" \
                "\n You see two areas you could search:")
            stuck = True
            dbell = False
            bolt = False
            broke = False
            while stuck:
                c3 = input(" 1 - Go to the shed"
                "\n 2 - Go to the nearby recreational area"
                "\n 3 - Try to break the fence")
                if c3 == "1":
                    print("You walk up to the shed and find that the door is locked")
                    c4 = input("Do you want to:"
                    "\n 1 - Go back"
                    "\n 2 - Search for a different way around")
                    if c4 == "2": 
                        if broke == False:
                            print("You look around the shed and find a boarded up window")
                            c5 = input("Do you want to:"
                            "\n 1 - Head back to the center of the courtyard"
                            "\n 2 - Try to break the boards on the window")
                            if c5 == "2":
                                if dbell:
                                    print("You break the boards on the window and can now enter")
                                    broke = True
                                    c6 = input("Do you want to:" \
                                    "\n 1 - Head back to the center of the courtyard" \
                                    "\n 2 - Enter the shed through the window")
                                    if c6 == "2":
                                        print("You enter the shed and find some bolt cutters laying on a work bench")
                                        c7 = input("Do you want to:" \
                                        "\n 1 - Head back to the center of the courtyard" \
                                        "\n 2 - Pick up the bolt cutters")
                                        if c7 == "2":
                                            dbell == False
                                            bolt == True
                                            print("You put down the dumbell and pick up the bolt cutters and then head back to the courtyard")
                                else:
                                    print("You punch the boards on the window and hear a crack come from your hand and the boards are fine" \
                                    "in doing so you decide to head back to the center of the courtyard")
                        elif broke == True: 
                            print("You look around the shed and find an open window")
                            c6 = input("Do you want to:"
                            "\n 1 - Head back to the center of the courtyard"
                            "\n 2 - Enter the window")
                            if c6 == "2":
                                if bolt == False:
                                    print("You enter the shed and find some bolt cutters laying on a work bench")
                                    c7 = input("Do you want to:" \
                                    "\n 1 - Head back to the center of the courtyard" \
                                    "\n 2 - Pick up the bolt cutters")
                                    if c7 == "2":
                                        dbell = False
                                        bolt = True
                                        print("You put down the dumbell and pick up the bolt cutters and then head back to the courtyard")
                                elif bolt == True:
                                    print("You enter the shed with the dumbell you placed down still" \
                                    " there and decide to head back to the center of the court yard")
                if c3 == "2":
                    if (dbell == True) or (bolt == True):
                        print("You walk over to the recreational area and find nothing of note and head back to the center of the courtyard")
                    else:
                        print("You walk over to the recreational area and find nothing of note and head back to the center of the courtyard")
                        print("You walk over to the recreational area and find a dumbell laying on the ground")
                        c4 = input("Do you want to" \
                        "\n 1 - Head back to the center of the courtyard" \
                        "\n 2 - Pick up the dumbell")
                        if c4 == "2":
                            print("You pick up the dumbell and head back to the center of the courtyard")
                            dbell = True
                if c3 == "3":
                    if bolt:
                        print("You cut open the fence and successfully escape the prison!")
                        stuck = False
                    elif dbell:
                        print("You hit the fence with the dumbell and it becomes slightly dented")
                    else:
                        print("You hit the fence... With your fists... Ouch")



if __name__ == "__main__":
    main()