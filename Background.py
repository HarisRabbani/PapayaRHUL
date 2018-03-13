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
        self.x = canvasW
        self.pos = pos
        self.pos.x = 0


    def update(self):
       # if self.pos.x < -self.width + self.canvasW:
        #    self.pos.x = self.width-self.canvasW
        self.pos.x %= -self.width
        self.pos.add(self.vel)
        print(self.pos.x)

    def draw(self, canvas):
        canvas.draw_image(self.img, (self.width / 2, self.height / 2), (self.width, self.height),(self.pos.getP()), (self.width, self.height))