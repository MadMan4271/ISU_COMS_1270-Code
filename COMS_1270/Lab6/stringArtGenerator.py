# Caden Burbridge       3/2/2026
# Lab 6 - This code creates art via strings

import py5
import random

def setup():
    py5.size(600, 600)
    py5.background(250,250,220)
    currentX = py5.width / 2
    currentY = py5.height / 2
    stepSize = 5
    shapeSize = 30
    steps = int(input("Please give a number of steps you would like to do: "))
    instr = generate_instructions(steps)
    py5.fill(0,0,0)
    for let in instr:
        if let == "U":
            currentY -= stepSize
        elif let == "D":
            currentY += stepSize
        elif let == "L":
            currentX -= stepSize
        elif let == "R":
            currentX += stepSize
        elif let == "C":
            py5.circle(currentX,currentY,shapeSize)
        elif let == "P":
            currentX = random.randint(0,600)
            currentY = random.randint(0,600)
        elif let == "K":
            py5.fill(random.randint(0,254),random.randint(0,254),random.randint(0,254))
        elif let == "S":
            stepSize = random.randint(1,10)
        elif let == "L":
            shapeSize = random.randint(1,100)

def generate_instructions(steps):
    # U: Move the current drawing location up on the canvas
    # D: Move the current drawing location down on the canvas
    # L: Move the current drawing location left on the canvas
    # R: Move the current drawing location right on the canvas
    # C: Draw a circle at the current drawing location on the canvas
    # P: Teleport the current drawing location to a random point on the canvas
    # K: Randomize the color of the fill for the circle
    # S: Randomize the step size from 1 to 10
    # L: Randomize the size of circles
    instr = ""
    choice = ['U','D','L','R','C','P','K','S','L']
    for i in range(1,steps+1):
        instr += choice[random.randint(0,(len(choice)-1))]
    return instr

        

if __name__ == "__main__":
    py5.run_sketch()