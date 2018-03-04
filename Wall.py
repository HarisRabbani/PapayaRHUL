try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import math
from Vector import Vector

class Wall:
    def __init__(self, x, border, color):
        self.x = x
        self.border = border
        self.color = color
        self.normal = Vector((1,0))
        self.edgeR = x + 1 + self.border
        self.edgeL = x - 1 - self.border

    def draw(self, canvas):
        canvas.draw_line((self.x, 0),
                         (self.x, 900),
                         self.border*2+1,
                         self.color)

    def hit(self, ball):
        hR = (ball.offsetL() <= self.edgeR)
        hL = (ball.offsetR() >= self.edgeL)
        return hR and hL