import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
from Sprite import Sprite


class Weapon(Sprite):

    def __init__(self, pos, vel, image, row, column):
            Sprite.__init__(image, row, column)
            self.pos = pos
            self.vel = vel

    def draw(self, canvas):
            canvas.draw_image(self.img, (self.x, self.y), (self.frameWidth, self.frameHeight),
                              self.pos.getP(), (50, 50), math.pi/2)
            # Code that does the sprite stuff.

    def bounce(self, normal):
            self.vel.reflect(normal)


    def update(self):
        super().update()
        self.pos.add(self.vel)





