try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

width = 500
height = 500


class Spritesheet:
    def __init__(self, url):
        self.img = simplegui.load_image(url)
        self.width=1500
        self.height=566
        self.rows = 5
        self.columns = 5
        self.frameWidth = 300
        self.frameHeight = 113.2
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.dimX = 300
        self.dimY = 113.2
        self.frameIndex = [4,4]  # maximum value
        self.newPos = (200,200)

    # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
    def draw(self, canvas):
        canvas.draw_image(self.img,
                          (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                           self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight),
                          self.newPos,
                          (self.dimX, self.dimY))

    def nextFrame(self):  # value can be passed to change the animation stating point
        # refers to the current frame index(assigning a value to it initially)

        self.frameIndex[0] = (self.frameIndex[0] + 1) % self.columns

        if self.frameIndex[0] == 0:
            self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows  # y is referred to by the rows




# s = Spritesheet('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png')

def randomExplosion():
    return (Spritesheet('http://personal.rhul.ac.uk/zeac/084/new_car_spritesheet.jpeg'))


explosions = [randomExplosion() for i in range(1)]


def draw(canvas):
    for i in explosions:
        i.draw(canvas)  # initial value passed to it
        i.nextFrame()
        # s.done()#canvas empty can be done with this
        # s.previousFrame()


frame = simplegui.create_frame("Main", width, height)
frame.set_canvas_background('white')
frame.set_draw_handler(draw)
frame.start()