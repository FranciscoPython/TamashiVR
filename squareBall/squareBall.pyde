def setup():
    strokeWeight(3)
    frameRate(42)
    size(650,650)
    
from random import randint
#import random.random
WIDTH=600
HEIGHT=600
x = 600
y = 600
vx = randint(-15,50)
vy = randint(-10,30)

   

def moveBall():    
  global x,y,vx,vy, WIDTH, HEIGHT

  fill(0, 102, 255)
  stroke(0)
  

  x=x+vx
  y=y+vy
  if x<0 or x>WIDTH:
    vx=-vx
    x=x+vx
  if y<120 or y>HEIGHT:
    vy=-vy
    y=y+vy 
  square(x,y,30)
  

draw = moveBall

def draw():
    background (0)
    if frameCount % 4 ==0:
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
    polygon(7, 300, 300, 50)

def polygon(n, cx, cy, r):
    angle = 360.0 / n
  
    beginShape();
    for i in xrange(n):
        vertex(cx + r * cos(radians(angle * i)),
          cy + r * sin(radians(angle * i)))
    endShape(CLOSE)



    stroke(255)
    strokeWeight(5)
   

    line(260,280,290,256)
    line(290,256,330,266)
    line(260,280,260,318)
    line(260,319,290,343)
    line(290,343,326,335)
    line(326,335,345,300)
    
    

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
