#from user301_kOICjXGLxt_0 import Vector
from Vector import Vector
import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Sprite import Sprite
width = 400
height = 400 
tick = 0
#((self.img.get_height())/2),((self.img.get_width())/2)    self.img.get_height,self.img.get_width    
class Bomb(Sprite):
   
    def __init__(self, x):
        self.k = random.randrange(500, 1200)
        self.pos = Vector((self.k, 0))
        self.vel = Vector((random.randint(-4, -2), random.randint(2, 4)))
        self.sprite = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Image_bomb.png') 
        self.image = simplegui.load_image('https://i.imgur.com/AD5CLP4.png')
        self.width = 1440 
        self.height = 1400 
        self.rows = 5 
        self.columns = 5 
        self.frameWidth = 589/5 
        self.frameHeight = 589/5
        self.frameCentreX = self.frameWidth/2 
        self.frameCentreY = self.frameHeight/2 
        self.canvasX = self.width/2 
        self.canvasY = self.height/2 
        self.dimX = 100 #Size of image/sprite on the canvas
        self.dimY = 100 
        self.frameIndex = [5, 4]


    def draw(self, canvas): 
        if(self.pos.y<=600):
            canvas.draw_image(self.image,
                          (97/2,100/2),
                          (97,100),
                          self.pos.getP(),
                          (self.dimX,self.dimY))
            
        if(self.pos.y>=600):
            canvas.draw_image(self.sprite, 
                          (self.frameWidth*self.frameIndex[0]+self.frameCentreX,self.frameHeight*self.frameIndex[1]+self.frameCentreY), 
                          (self.frameWidth, self.frameHeight), 
                          self.pos.getP(), 
                          (self.dimX, self.dimY)) 

       
                    
                    
    def nextFrame(self): 
        self.frameIndex[0]= (self.frameIndex[0]+1)%self.columns 
        if self.frameIndex[0] == 0: 
            self.frameIndex[1]=(self.frameIndex[1]+1)%self.rows 
    def update(self):
        self.pos.add(self.vel)

        self.nextFrame()

    def hit(self, car):
        T = Vector((self.pos.x, self.pos.y - self.frameHeight / 2))
        B = Vector((self.pos.x, self.pos.y + self.frameHeight / 2))
        R = Vector((self.pos.x + self.frameWidth / 2, self.pos.y))
        L = Vector((self.pos.x - self.frameWidth / 2, self.pos.y))

        for i in car.offsets:
            if i.x > L.x and i.x < R.x:
                 if i.y > T.y and i.y < B.y:
                     return True

  




