try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Sprite:
    #Parent class for anything that has a spritesheet

    def __init__(self, image, row, column):
        self.img = image
        self.row = row
        self.column = column
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.frameHeight = self.height // self.row
        self.frameWidth = self.width // self.column
        self.frameCenterX = self.frameWidth / 2
        self.frameCenterY = self.frameHeight / 2
        self.x = None
        self.y = None
        self.hitCount = 0
        self.frameIndex = [0, 0]
        self.set_frame()
        self.animate = False

    def offsetL(self):
        return self.pos.x - self.width / 2

    def offsetR(self):
        return self.pos.x + self.width / 2

    def update(self):
        if (self.animate == False) or (self.update_x() and self.update_y()):
            self.frameIndex[0] = 0
            self.frameIndex[1] = 0
            self.update_x()
            self.update_y()
            print(self.frameIndex)

        else:
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
