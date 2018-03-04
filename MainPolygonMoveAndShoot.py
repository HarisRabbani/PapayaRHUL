from user301_dZJL5znAdk_0 import Vector
from user301_uxLQLcWnDf_99 import RegularPolygon
from user301_FM91pKbpyD_3 import Keyboard
from user301_n8rcr25g0U_0 import Particle

import simplegui


CANVAS_WIDTH = 2000
CANVAS_HEIGHT = 2000

kbd = Keyboard()
pentagon = RegularPolygon(2, Vector(250, 250), 100, kbd,CANVAS_WIDTH,CANVAS_HEIGHT )
particles = []


def draw(canvas):
    if kbd.space:
        p = Particle(pentagon.pos + pentagon.generator, pentagon.generator.getNormalized())
        particles.append(p)
    

    for p in particles:
        p.draw(canvas)
        p.update()
   
    pentagon.draw(canvas)
    pentagon.drawGenerator(canvas)
    pentagon.update()
   
    
    
    

frame = simplegui.create_frame('Control', CANVAS_WIDTH, CANVAS_HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
frame.start()