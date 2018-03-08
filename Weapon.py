import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math

class Weapon:

    def __init__(self, pos, vel, image, row, column):
            self.pos = pos
            self.vel = vel
            self.sprite = simplegui.load_image(image)
            self.width = self.sprite.get_width()
            self.height = self.sprite.get_height()
            self.row = row
            self.column = column
            self.explosion = False
            self.frameClock = 1/60
            self.frameHeight = self.height//self.row
            self.frameWidth = self.width//self.column
            self.frameCenterX = self.frameWidth / 2
            self.frameCenterY = self.frameHeight / 2
            self.x = None
            self.y = None
            self.hitCount = 0
            self.frameIndex = [0, 0]
            self.set_frame()

    def draw(self, canvas):
            canvas.draw_image(self.sprite, (self.x, self.y), (self.frameWidth, self.frameHeight),
                              self.pos.getP(), (50, 50), math.pi/2)

    def bounce(self, normal):
            self.vel.reflect(normal)

    def offsetL(self):
        return self.pos.x - self.width/2

    def offsetR(self):
        return self.pos.x + self.width/2

    def update(self):
        if self.explosion:
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.column
            self.update_x()
            if self.frameIndex[0] == 0:
                self.frameIndex[1] = self.frameIndex[1] + 1
                self.update_y()
        else:
            self.pos.add(self.vel)

    def set_frame(self):
        # Initial position, this will hold true until explosion
        self.update_x()
        self.update_y()

    def update_x(self):
        self.x = self.frameWidth * self.frameIndex[0] + self.frameCenterX

    def update_y(self):
        self.y = self.frameHeight * self.frameIndex[1] + self.frameCenterY



