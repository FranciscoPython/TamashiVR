global angle
angle = 0

def setup():
    size(650, 650)

def drawPoly():
    global angle
    pushMatrix()
    translate(width/2, height/2)
    rotate(radians(angle))
    polygon(300, 4, 4)
    popMatrix()
    

def rpoly():
    global angle
    if keyPressed and keyCode==RIGHT:
        angle= angle+1
        #drawPoly()
    if keyPressed and keyCode==LEFT:
        angle= angle-1
        #drawPoly()
        
    
    
def draw():
    background(0)
    drawPoly()
    rpoly()
    #polygon(300, 4, 4)



    # with pushMatrix():
    #     translate(width-9, height -9)
    #     rotate(frameCount / -10.0)
    #     polygon(300, 4, 4)


def polygon(x, y, radius):
    beginShape();
    stroke(255)
    strokeWeight(8)
    line(260-300,280-300,290-300,256-300)
    line(290-300,256-300,330-300,266-300)
    line(260-300,280-300,260-300,318-300)
    line(260-300,319-300,290-300,343-300)
    line(290-300,343-300,326-300,335-300)
    line(326-300,335-300,345-300,300-300)
    endShape() 

    # line(260,280,290,256)
    # line(290,256,330,266)
    # line(260,280,260,318)
    # line(260,319,290,343)
    # line(290,343,326,335)
    # line(326,335,345,300)

    
    endShape()
