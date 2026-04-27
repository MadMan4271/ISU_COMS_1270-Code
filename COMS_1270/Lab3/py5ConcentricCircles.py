# Caden Burbridge                       02/09/2026
# Lab week 3 - This sketches multiple circles around the same point which changes colors each iteration

import py5

def green():
    py5.fill(0,115,0)

def blue():
    py5.fill(150,200,255)

def beige():
    py5.fill(250,250,220)

def concentricCircles(r, x, y):
    rad = r
    for i in range((r-30) // 30):
        py5.no_stroke()
        # Circle colors cycle from Green --> Blue --> Beige and then back to the start
        if (i % 3) == 1:
            py5.fill(0,115,0)
        elif (i % 3) == 2:
            py5.fill(150,200,255)
        else:
            py5.fill(250,250,220)
        py5.circle(x, y, rad)
        rad -= 30

def setup():
    py5.size(600, 600)
    py5.background(250,250,220)

    while True :
        r = int(input("What is the radius of the largest circle (at least 240): "))
        if r < 240:
            r = int(input("What is the radius of the largest circle: "))
        elif r >= 240:
            break
    x = int(input("What x coordinate should the circles be centered around: "))
    y = int(input("What y coordinate should the circles be centered around: "))

    concentricCircles(r, x, y)

if __name__ == "__main__":
    py5.run_sketch()