# Caden Burbridge       3/29/2026
# Lab 7 - This code simulates bubbles floating to the top in water

import py5 

import random

bx = []
by = []

def setup():
    py5.size(600,400)
    for i in range(0,30):
        bx.append(random.randint(1,600))
        by.append(random.randint(1,400))

def draw():
    py5.background(0,0,50)
    py5.fill(150,150,240)
    for i in range(0, len(bx)):
        py5.circle(bx[i],by[i],30)
        by[i] -= 5
        if by[i] <= 0:
            by[i] = random.randint(1,400)

if __name__ == "__main__":
    py5.run_sketch()