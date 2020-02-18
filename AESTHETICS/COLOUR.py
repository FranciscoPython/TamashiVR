    if frameCount%120 == 0:
        stroke(8, 3, 61) 
        fill (8, 3, 61, 80)
        rect (10,200,width-20, height-50)
        stroke(255, 255, 0, ) 
        fill( 255, 255, 255, 0)
        for i in range(250):
            Xpos = random(15, 485)
            Ypos = random (202,485)
            Size = random (.1,.5)
            circle( Xpos, Ypos, Size)
    if frameCount%360 ==0:
        stroke(8, 3, 61) 
        fill (8, 3, 61, 50)
        rect (10,200,width-20, height-50)
