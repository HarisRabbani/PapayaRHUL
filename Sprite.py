try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
from Vector import Vector
from Offset import Offset

class Sprite(Offset):
    #Parent class for anything that has a spritesheet

    def __init__(self, image, row, column, pos):
        self.img = image
        self.row = row
        self.column = column
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.frameHeight = self.height // self.row
        self.frameWidth = self.width // self.column
        self.frameCenterX = self.frameWidth / 2
        self.frameCenterY = self.frameHeight / 2
        self.offsetA = 0  # Used to approximate hitboxes for sprites with bad ones
        self.x = None
        self.y = None
        self.hitCount = 0
        self.frameElapsed = 0
        self.frameIndex = [0, 0]
        self.set_frame()
        self.animate = False
        self.corners = [None, None, None, None]  # This will hold all the corner posistions of any sprite
        self.offsets = [None, None, None, None]  # This will hold all of the offsets UP, DOWN, LEFT, RIGHT
        self.defineOffsets(pos)
        super().__init__(self.offsets[0], self.offsets[1], self.offsets[2], self.offsets[3])


    def defineOffsets(self, pos):
        self.offT = Vector((pos.x, pos.y - self.frameHeight/2))
        self.offB = Vector((pos.x, pos.y + self.frameHeight/2))
        self.offR = Vector((pos.x + self.frameWidth/2, pos.y))
        self.offL = Vector((pos.x - self.frameWidth/2, pos.y))

        self.offsets[0] = self.offT
        self.offsets[1] = self.offB
        self.offsets[2] = self.offR
        self.offsets[3] = self.offL

    def defineCorners(self, pos):
        tL = Vector((pos.x - self.frameWidth/2, pos.y - self.frameHeight/2))
        tR = Vector((pos.x + self.frameWidth/2, pos.y - self.frameHeight/2))
        bR = Vector((tL.x, pos.y + self.frameHeight/2))
        bL = Vector((tR.x, bR.y))

        self.corners[0] = tL
        self.corners[1] = tR
        self.corners[2] = bR
        self.corners[3] = bL

    def update(self):  # Make edits to this to fix the bug
        if (self.animate == False) or (self.update_x() and self.update_y()):
            self.frameIndex[0] = 0
            self.frameIndex[1] = 0
            self.update_x()
            self.update_y()


        else:
            self.frameElapsed += 1
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.column
            self.update_x()
            if self.frameIndex[0] == 0:
                self.frameIndex[1] = self.frameIndex[1] + 1
                self.update_y()


    def maxFrame(self):
        return self.frameIndex==0


    def set_frame(self):
        # Initial position, this will hold true until explosion
        self.update_x()
        self.update_y()

    def update_x(self):
        if self.frameIndex[0] == self.column-1:
            return True
        else:
            self.x = self.frameWidth * self.frameIndex[0] + self.frameCenterX

    def update_y(self):
        if self.frameIndex[1] == self.column-1:
            return True
        else:
            self.y = self.frameHeight * self.frameIndex[1] + self.frameCenterY
