from user301_dZJL5znAdk_0 import Vector
import random

def randCol():
    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)
    return 'rgb('+str(r)+ ','+str(g)+ ','+str(b)+ ')'

class Particle:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.radius = 10
        self.colour = randCol()
        
    def draw(self, canvas):
        canvas.draw_circle(self.pos.getP(), self.radius, 1, self.colour, self.colour)
        
    def bounce(self, normal):
        self.vel.reflect(normal)
        
    def update(self):
        self.pos.add(self.vel)
