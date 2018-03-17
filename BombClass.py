#from user301_kOICjXGLxt_0 import Vector
from Vector import Vector
import random
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

width = 400
height = 400 
tick = 0
#((self.img.get_height())/2),((self.img.get_width())/2)    self.img.get_height,self.img.get_width    
class Bomb:
   
    def __init__ (self, sprite, pos, radius=10): 
        self.k = random.randrange(50,350)
        self.pos = Vector(self.k,50)
        self.vel = Vector()
        self.sprite = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Image_bomb.png') 
        self.image = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Image_bomb_single.jpeg')
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
        if(self.pos.y<=350):
            canvas.draw_image(self.image,
                          (218/2,224/2),
                          (218,224),
                          self.pos.getP(),
                          (self.dimX,self.dimY))
            
        if(self.pos.y>=350):
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
        self.vel.multiply(0.85)
        self.nextFrame()
        if(self.pos.y<=350):
            self.vel.add(Vector(0,0.45))
        
        if(self.pos.y >= 350):
            self.vel.add(Vector(-0.5,0))
  


  

k = Bomb(Vector(width/2,height/2), 40)

def draw(canvas):
    k.draw(canvas)
    k.update()

frame = simplegui.create_frame('Interactions', width, height)
frame.set_draw_handler(draw)
frame.set_canvas_background('White')
frame.start()

