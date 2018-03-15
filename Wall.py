try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import math
from Vector import Vector

class Wall:
    def __init__(self, arg1, arg2,  border, color, normal):
        self.arg1 = arg1
        self.arg2 = arg2
        self.border = border
        self.color = color
        self.normal = normal
        self.edgeR = arg1[0] + 1 + self.border
        self.edgeL = arg1[0] - 1 - self.border

    def draw(self, canvas):
        canvas.draw_line(self.arg1, self.arg2, self.border*2+1,  self.color)

    def hit(self, ball):
        hR = (ball.offsetL <= self.edgeR)
        hL = (ball.offsetR >= self.edgeL)
        return hR and hL