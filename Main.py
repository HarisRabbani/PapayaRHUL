
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
from Weapon import Weapon
from WeaponCollision import WeaponCollision
from Wall import Wall
import random

CANVAS_WIDTH = 1600
CANVAS_HEIGHT = 900

rockets = []

C = WeaponCollision()
w2 = Wall(500, 5, 'red')
w4 = Wall(1200, 5, 'red')

C.addWall(w2)
C.addWall(w4)

def spawn(key):
    global CANVAS_WIDTH, CANVAS_HEIGHT
    if key == simplegui.KEY_MAP['space']:
        missile = Weapon(Vector((CANVAS_WIDTH/2, CANVAS_HEIGHT/2)), Vector((random.randint(-5,5), random.randint(-5,5))), 'https://i.imgur.com/RVi7F76.png',
                         4, 4)
        C.addWeapon(missile)


def up(key):
   pass


def draw(canvas):
    global CANVAS_WIDTH, CANVAS_HEIGHT
    if rockets.__len__() == 5:
        rockets[0].explosion = True
    for missile in rockets:
        if missile.explosion:
            C.weapons.remove(missile)
        else:
            missile.update()
            missile.draw(canvas)





frame = simplegui.create_frame("Test", CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(C.draw)
frame.set_keydown_handler(spawn)
frame.set_keyup_handler(up)

# Start the frame animation
frame.start()