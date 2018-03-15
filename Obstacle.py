from Sprite import Sprite


class Obstacle(Sprite):
    def __init__(self, pos, vel, image):
        self.img = image
        super().__init__(image, 3, 3)
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.pos = pos
        self.vel = vel

    def update(self):
        super().update()
        self.pos.sub(self.vel)
        super().defineOffsets(self.pos)
        super().defineCorners(self.pos)

    def draw(self, canvas):
        canvas.draw_image(self.img, (self.x, self.y), (self.frameWidth, self.frameHeight), self.pos.getP(),(self.frameWidth, self.frameHeight))