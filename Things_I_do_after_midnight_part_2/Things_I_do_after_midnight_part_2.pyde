def setup():
    global particle
    global listparticle
    listparticle = []
    size(400,400)
    for i in range (10):
        particle = Particle() # this instanciate the class particle
        particle.randomize()
        listparticle.append(particle)
            # particle = Particle() # this instanciate the class particle
            # particle.randomize()
    
def draw():
    background(9, 11, 61)
    stroke(241, 252, 20)
    fill(241, 252, 20)
    for i in range(10):
        listparticle[i].draw_it()
        listparticle[i].move()
        for j in range(9):
            line(listparticle[i].pos_x,listparticle[i].pos_y,listparticle[j].pos_x,listparticle[j].pos_y)
class Particle:
    def __init__(self):
        self.pos_x = 40
        self.pos_y = 40
        self.velo_x = .01
        self.velo_y = .01

    def randomize(self):
        # should randomize position x from 0 to width
        self.pos_x = random(40,380)
        
        # position y from 0 to height
        self.pos_y = random(40,380)
        print(self.pos_x)
        print(self.pos_y)
        
        # velocity x from -5 to 5
        self.velo_x = random(-5,1)
        
        # velocity y from -5 to 5
        self.velo_x = random(-5,1)


    def move(self):
        # Should move the particle according to its velocity.
        self.pos_x = self.pos_x + self.velo_x
        self.pos_y += self.velo_y
        
        # Should wrap around the screen if off limits.
        if self.pos_x > 380:
            #self.velo_x *= -1
            self.pos_x = 0
            
        if self.pos_x < 0:
            #self.velo_x *= -1
            self.pos_x = 380
            
        if self.pos_y > 380:
            #self.velo_y *= -1
            self.pos_y = 0
            
        if self.pos_y < 0:
            #self.velo_y *= -1
            self.pos_y = 380

    
    def draw_it(self):
        # Should draw a circle where the particle is.
#        square(self.pos_x,self.pos_y,10)
        circle(self.pos_x,self.pos_y,10)

        stroke (126, 133, 252)

        textSize(14);    
        text("CRAZY THINGS I DO AFTER MIDNIGHT",80,13)
   
        fill (126, 133, 252)    
        textSize(10);
        text("THE DISASTER MAKEUP ASSIGNMENT",121,30)
        textSize(8);
        fill (250, 245, 245)   
    
#        fill(241, 252, 20)
        rect(-1, 16, width+1, .5)   

        rect(-1, 380, width+1, .5)    
