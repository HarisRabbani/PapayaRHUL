try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.space = False
        self.up = False
        self.down = False
        self.w = False
        self.a = False
        self.s = False
        self.d = False
        self.f = False


        self.activeMissile = False
        self.count=2

    def keyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True
        if key == simplegui.KEY_MAP['up']:
            self.up = True
        if key == simplegui.KEY_MAP['down']:
            self.down = True
        if key == simplegui.KEY_MAP['w']:
            self.right = True
        if key == simplegui.KEY_MAP['a']:
            self.left = True
        if key == simplegui.KEY_MAP['s']:
            self.space = True
        if key == simplegui.KEY_MAP['d']:
            self.up = True
        if key == simplegui.KEY_MAP['f']:
            self.down = True

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['space']:
            self.space = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
        if key == simplegui.KEY_MAP['down']:
            self.down = False
        if key == simplegui.KEY_MAP['w']:
            self.right = False
        if key == simplegui.KEY_MAP['a']:
            self.left = False
        if key == simplegui.KEY_MAP['s']:
            self.space = False
        if key == simplegui.KEY_MAP['d']:
            self.up = False
        if key == simplegui.KEY_MAP['f']:
            self.down = False
