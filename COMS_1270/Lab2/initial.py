import py5
r = 30
    
    #Diagonal Rectangle
    # py5.push_matrix()
    # py5.translate(50,50) <--- shifts the rectangle as if it werent rotated
    # py5.rotate(py5.radians(45))
    # py5.rect(300,0,220,50)
    # py5.pop_matrix()

#Green circle
def circ1(x,y,r):
    py5.no_stroke()
    py5.fill(0,115,0)
    py5.circle(x,y,r)

#Blue circle
def circ2(x,y,r):
    py5.no_stroke()
    py5.fill(150,200,255)
    py5.circle(x,y,r)

#Beige Circle
def circ3(x,y,r):
    py5.no_stroke()
    py5.fill(250,250,220)
    py5.circle(x,y,r)

def rectangle(x,y,width,height,rotation,color):
    py5.push_matrix()    
    if color == "green":
        py5.fill(0,115,0)
    elif color == "blue":
        py5.fill(150,200,255)
    else:
        py5.fill(250,250,220)

    py5.no_stroke()
    py5.rotate(py5.radians(rotation))
    py5.rect(x,y,width,height)
    py5.pop_matrix()


def setup():
    py5.size(600, 600)
    py5.background(250,250,220)

#X+ right
#Y+ down

def draw():
    t = 90
    #letter C
    circ1(150+t,275,300)
    circ3(150+t,275,230)
    

    #letter B
    circ2(300+t,200,150)
    circ2(300+t,350,150)
    circ3(300+t,200,85)
    circ3(300+t,350,85)
    rectangle(225+t,125,75,300,0,"")
    rectangle(265+t,125,35,300,0,"blue")

py5.run_sketch()