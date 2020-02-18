import BallClass
import BrickClass
padpos = -10
padpos1 = 0   
key_mode = 0
global img


def draw():
    image(img, 250, 350)
    img = loadImage
    loadImage("th.jpg")
def setup():



    size(500,500)
    global img
       
    background(14, 7, 250)

        
    global ball
    global Bricks

#
    
    Bricks = [] 
    for i in range(10):    #drawing bricks 10 columns wide
        for j in range(8): #drawing bricks 8 rows high
            brick1 = BrickClass.Brick(9 + i*48, 50+j*25, 48, 22) #coordinates for the first brick 
            Bricks.append(brick1) 
    ball = BallClass.Ball(200, 441) 

          
def paddle():
    fill(8, 11, 239)
    stroke(7, 122, 250)
    circle(padpos, 463, 15)
    circle(padpos + 30, 463, 15)
    rect(padpos, 455, 30, 15)

def draw():

    global ball
    global Bricks
    background(12, 14, 152)
    fill(4, 19, 94)
    rect(-1, 0, width+1, 40)#upperframe
    rect(-1, 464, width+1, 40)#upperframe
    ball.draw()
    for i in range(len(Bricks)):
        if Bricks[i].hit_test(ball.pos_x, ball.pos_y):
            Bricks[i].erase()
        Bricks[i].draw()
    global padpos1
    global key_mode
    if keyPressed:
        key_mode = 1
        if ball.dx == 0 and key == " ":
            ball.dx = 4
            ball.dy = -6
    if mousePressed:
        key_mode = 0
        if ball.dx ==0:
            ball.dx = 2 
            ball.dy = -2
    if key_mode == 0:
        padpos1 = mouseX
    if key_mode == 1:     
        if keyPressed:
            if keyCode == LEFT:
                padpos1 = padpos1 - 10
                
            if keyCode == RIGHT:
                padpos1 = padpos1 + 10  
    if padpos1 >= 470: 
        padpos1 = 470                
    if padpos1 <= 30: 
        padpos1 = 30
    if ball.dx ==0:
        ball.pos_x = padpos1
    pushMatrix()
    translate(padpos1,1)       
    paddle()
    popMatrix()
    ball.padpos = padpos1       

    textSize(14);    
    text("CRAZY THINGS I DO AFTER MIDNIGHT",200,30)  
    fill (2, 77, 159)
    textSize(12);
    text(mouseX,470,15);   
    text(mouseY,470,28); 
    textSize(12);    
    text("AESTHETIC GAME DESIGN DEVELOPMENT",250,485) 
    img = loadImage("th.jpg") 
