try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector


class Tree:

    def __init__(self, img, y, canvasW):
        self.img = img
        self.width = img.get_width()
        self.height = img.get_height()
        self.vel = Vector((-1, 0))
        self.canvasW = canvasW
        self.x = canvasW
        self.y = y
        self.pos = Vector((self.x, self.y))

    def update(self):
        if self.pos.x < 0 - self.width:
            self.pos.x = self.canvasW + self.width

        self.pos.add(self.vel)

    def draw(self, canvas):
        canvas.draw_image(self.img, (self.width/2, self.height/2), (self.width, self.height),
                          (self.pos.getP()), (self.width, self.height))
