from SpriteSheet import Spritesheet


class Obstacle(Spritesheet):
    def __init__(self, pos, vel, image):
        self.img = image
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.pos = pos
        self.vel = vel


