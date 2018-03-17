try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
from Sprite import Sprite


class Background:

    def __init__(self, img, pos, canvasW):
        self.img = img
        self.width = img.get_width()
        self.height = img.get_height()
        self.vel = Vector((-1, 0))
        self.canvasW = canvasW
        self.x = 0
        self.pos = pos
        self.pos.x = canvasW + (self.width/2 - canvasW)


    def update(self):
       # if self.pos.x < -self.width + self.canvasW:
        #    self.pos.x = self.width-self.canvasW
       # self.pos.x %= -self.width

        self.x = self.pos.x - self.width/2
        if self.x < -self.width+self.canvasW:
            self.pos.x = self.canvasW + (self.width/2 - self.canvasW)
        self.pos.add(self.vel)


    def draw(self, canvas):
        canvas.draw_image(self.img, (self.width / 2, self.height / 2), (self.width, self.height),(self.pos.getP()), (self.width, self.height))