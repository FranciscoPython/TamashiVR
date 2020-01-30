def setup():
    background(0)
    size(400,400)
    ellipse(150,200,20,20)


def draw():
    background (0)
    fill (194, 4, 20)    
    text("CRAZY THINGS I DO AFTER MIDNIGHT",13,13)
   
    fill (252, 148, 3)    
    text("THE POLYGON MADNESS ASSIGNMENT",13,25)
    #text((mouseX + "," + mouseY), 250,300);   
    fill (250, 245, 245)
    text(mouseX,300,13);   
    text(mouseY,350,13);   
 
    stroke(255)
    strokeWeight(5)
    line(180,300,140,250)
    line(230,280,180,300)
    line(225,225,200,200)
    line(200,200,140,250)
    
    ellipse(150,200,15,15)
    

      
