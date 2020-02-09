"""
Rotate 1. 

Rotating simultaneously in the X and Y axis. 
Transformation functions such as rotate() are additive.
Successively calling rotate(1.0) and rotate(2.0)
is equivalent to calling rotate(3.0). 
"""

a = 0.0


def setup():
    size(650, 650, P3D)
    global rSize
    rSize = width / 1
    noStroke()
    fill(0)


def draw():
    global a
    background(0)

    a += .05
    if a > 20:
        a = 1

    translate(width / 2, height / 2)

    #rotateY(a)
    rotateX(a)
    fill(255)
    
    beginShape();



    stroke(255)
    strokeWeight(8)

    line(260,280,290,256);
    line(290,256,330,266);
    line(260,280,260,318);
    line(260,319,290,343);
    line(290,343,326,335);
    line(326,335,345,300);
    line(326,335,345,300);
    endShape();
