
a = 3


def setup():
    size(650, 650, P3D)
    global rSize
    rSize = width / 2
    noStroke()
    fill(0)


def draw():
    global a
    background(0)

    a += .05
    if a > 30:
        a = 3

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
