def setup():
    background(55)
    size(400,400)

def pipes():
    rect(x, y - 500,10,800)
    rect(x, y + 350,10,800)
def bird():
    rect(e,d,4,4)
y = 0    
x = 300   
def draw():
    global x
    global y 
    background (55) 
    pipes()
    x = x - 4
    y = y - 1
    
    if x == 0:
        x = 400
    if y == -340:
        y = 0
        

        


     


    
