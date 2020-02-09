

def setup():
    size(650, 650)


def draw():
    background(0)



    with pushMatrix():
        translate(width-9, height -9)
        rotate(frameCount / -10.0)
        polygon(300, 4, 4)


def polygon(x, y, radius):
    beginShape();
    stroke(255)
    strokeWeight(8)
   

    line(260,280,290,256)
    line(290,256,330,266)
    line(260,280,260,318)
    line(260,319,290,343)
    line(290,343,326,335)
    line(326,335,345,300)
    endShape()
