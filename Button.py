try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Button:

    def __init__(self, image, pos, trigger):
        self.image = simplegui.load_image(image)
        self.pos = pos
        self.trigger = trigger
        self.clicked = False

    def draw(self, canvas):
        canvas.draw_image(self.image, (self.image.get_width() / 2, self.image.get_height() / 2),(self.image.get_width(), self.image.get_height()), self.pos,(self.image.get_width(), self.image.get_height()))

    def contains(self, pos):
        return self.pos[0] - (self.image.get_width() / 2) < pos[0] < self.pos[0] + (self.image.get_width() / 2) and \
               self.pos[1] - (self.image.get_height() / 2) < pos[1] < self.pos[1] + (self.image.get_height() / 2)

    def clickBtn(self):
        self.clicked = True
        self.trigger()