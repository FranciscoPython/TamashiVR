global angle
angle = 0

from random import randint
#import random.random
WIDTH=600
HEIGHT=600
x = 600
y = 600
vx = randint(-15,140)
vy = randint(-10,30)



def setup():
    strokeWeight(3)
    frameRate(20)
    size(650,650)
    
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
        angle= angle+8
        #drawPoly()
    if keyPressed and keyCode==LEFT:
        angle= angle-8
        
def moveBall():    
  global x,y,vx,vy, WIDTH, HEIGHT

  fill( 255,255,0)
  stroke(0)
  

  x+=vx
  y=y+vy
  if x<0 or x>WIDTH:
    vx=-vx
    x=x+vx
  if y<150 or y>HEIGHT:
    vy=-vy
    y=y+vy 
  circle(x,y,30)
  



def draw():
    background (0)
    
    if frameCount % 2==1:
        #up-
        moveBall()
    fill (194, 4, 20)
    textSize(14);    
    text("CRAZY THINGS I DO AFTER MIDNIGHT",180,13)
   
    fill (252, 148, 3)    
    textSize(19);
    text("THE POLYGON MADNESS ASSIGNMENT",121,30)
    textSize(12);
    fill (250, 245, 245)
    

    text("SCORE",30,13)
    textSize(25);
    text(mouseX,30,45);
    #text((mouseX + "," + mouseY), 250,300);   
    fill (250, 245, 245)
    textSize(12);
    text(mouseX,500,25);   
    text(mouseY,550,25);
  
    fill(55)
    stroke(5)
    #pushMatrix()
    # translate(width/2, height/2)
    # rotate(radians(angle))
    # #polygongris(7, 300, 300, 50)
    # polygongris(7, 300, 4, 4)
    # popMatrix()
    polygongrey(7, 329, 329, 50)
    drawPoly()
    rpoly()

def polygongrey(n, cx, cy, r):
    angle = 360.0 / n
  
    beginShape();
    for i in xrange(n):
        vertex(cx + r * cos(radians(angle * i)),
          cy + r * sin(radians(angle * i)))
    endShape(CLOSE)


    # beginShape();
    # stroke(255)
    # strokeWeight(5)
   

    # line(260,280,290,256)
    # line(290,256,330,266)
    # line(260,280,260,318)
    # line(260,319,290,343)
    # line(290,343,326,335)
    # line(326,335,345,300)
    # endShape()
    

    stroke(1) 
    fill (0)
    if frameCount % 1 ==0:
    #if frameRate %11 >= 9:
        stroke(0 ) 
        fill( 255,255,0)
        Xpos = random(0, 600)
        Ypos = random (60,100)
        Size = random (10,80)
        circle(Xpos, Ypos, Size)
        fill (252, 148, 3)    

        fill (194, 4, 20)

        textSize(50);
      
        text("JACK POT",180,530)
