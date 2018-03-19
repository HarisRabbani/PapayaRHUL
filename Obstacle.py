from Sprite import Sprite
from Vector import Vector

class Obstacle(Sprite):
    def __init__(self, pos, vel, image, row, column):
        self.img = image
        super().__init__(image, row, column, pos)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.pos = pos
        self.vel = vel
        self.frameCount = 0
        self.removeSelf = False

    def animateOnce(self):
        self.animate = True
        while self.frameElapsed < self.row * self.column:
            super().update()
        self.animate = False

    def update(self):

        if self.animate:

            self.frameCount += 1
            if self.frameCount % 5 == 0:
                super().update()
        else:
            super().update()
        self.pos.add(self.vel)
        super().defineOffsets(self.pos)
        super().defineCorners(self.pos)


    def draw(self, canvas):
        canvas.draw_image(self.img, (self.x, self.y), (self.frameWidth, self.frameHeight), self.pos.getP(),(self.frameWidth, self.frameHeight))
