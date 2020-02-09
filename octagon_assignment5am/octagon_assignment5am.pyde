def setup():
    background(66)
    size(400,400)


def draw():
    background (66)
    text("cool",13,13)
    #text((mouseX + "," + mouseY), 40,13);   
    text(mouseX,40,13);   
    text(mouseY,80,13);   
 
    stroke(255)
    strokeWeight(5)
    line(200,100,140,150)
    ellipse(150,200,20,20)
    ellipse(221,183,80,80)
    
    line(200,100,140,50)
    line(200,200,140,150)
    line(200,200,140,250)
    

      
