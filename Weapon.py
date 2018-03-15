import Vector
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
from Sprite import Sprite


class Weapon(Sprite):

    def __init__(self, pos, vel, image, row, column):
            super().__init__(image, row, column, pos)
            self.pos = pos
            self.vel = vel
            super().defineOffsets(self.pos)
            super().defineCorners(self.pos)


    def draw(self, canvas):
            canvas.draw_image(self.img, (self.x, self.y), (self.frameWidth, self.frameHeight),
                              self.pos.getP(), (50, 50), math.pi/2)
            for i in self.offsets:
                canvas.draw_point(i.getP(), "Black")
            # Code that does the sprite stuff.

    def bounce(self, normal):
            self.vel.reflect(normal)


    def update(self):
        super().update()
        super().defineOffsets(self.pos)
        super().defineCorners(self.pos)
        self.pos.add(self.vel)





