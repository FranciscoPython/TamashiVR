def setup():
    size(600, 600)
    background(0)
    

def draw():
    background (0)
    fill (194, 4, 20)
    textSize(14);    
    text("CRAZY THINGS I DO AFTER MIDNIGHT",180,13)
   
    fill (252, 148, 3)    
    textSize(19);
    text("THE POLYGON MADNESS ASSIGNMENT",121,30)
    textSize(12);
    fill (250, 245, 245)
    text("SCORE",30,13)
    textSize(30);
    text(mouseX,30,45);
    #text((mouseX + "," + mouseY), 250,300);   
    fill (250, 245, 245)
    textSize(12);
    text(mouseX,500,25);   
    text(mouseY,550,25);

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

    if frameRate %10 >= 9:
        stroke(0 ) 
        fill( 255,255,0)
        Xpos = random(0, 600)
        Ypos = random (100,500)
        Size = random (10,80)
        circle(Xpos, Ypos, Size)
        fill (252, 148, 3)    

        fill (194, 4, 20)

        textSize(50);
      
        text("JACK POT",180,530)



    
