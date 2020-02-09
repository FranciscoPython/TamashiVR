
    



def setup():
    size(500,500)

def draw():

    stroke(1) 
    fill (0)

    if frameCount %1000 > 0:
        stroke(0 ) 
        fill( 255,255,0)
        Xpos = random(45, 448)
        Ypos = random (40,448)
        Size = random (4,50)
        circle(Xpos, Ypos, Size)

        



    
