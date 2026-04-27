# Caden Burbridge 2/26/2026
# Lab 5 - This file creates a grid of squares with a inputed side length
import py5
import random

def py52DQuilt(x,y,s):
    for i in range(0, x):
        for j in range(0, y):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            py5.fill(r, g, b)
            py5.rect(s * i, s * j, s, s)

def setup():
    py5.size(600, 600)
    py5.background(250,250,220)
    x = int(input("Please give a x coordinate: "))
    y = int(input("Please give a y coordinate: "))
    s = int(input("Please give a square side length: "))
    py52DQuilt(x,y,s)

def main():
    x = int(input("Please give a x coordinate: "))
    y = int(input("Please give a y coordinate: "))
    s = int(input("Please give a square side length: "))
    py52DQuilt(x,y,s)

if __name__ == "__main__":
    py5.run_sketch()