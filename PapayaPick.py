try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector
from Vector import Vector

from Sprite import Sprite

class PapayaPick(Sprite):


    def __init__(self,img,pos,width,height, vel):
        self.img = img
        super().__init__(img, 1,1, pos)
        self.pos=pos
        self.vel=vel
        self.width=width
        self.height=height


    def draw(self,canvas):
        canvas.draw_image(self.img, (self.width/2,self.height/2), (self.width,self.height), (self.pos.getP()), (50, 50))




    def update(self):
        self.pos.add(self.vel)

        super().update()
        super().defineOffsets(self.pos)
        super().defineCorners(self.pos)

        #possible code used for the collision detection with the car
"""
        if (self.touchPapaya) == False:
            if ((obj_user_car.pos.x + car_width > papaya_x) and obj_user_car.pos.x < papaya_x + papaya_size):
                if (papaya_y < obj_user_car.pos.y and papaya_y + papaya_size < obj_user_car.pos.y) or \
                        (obj_user_car.pos.y < papaya_y + papaya_size) and (obj_user_car.pos.y < papaya_y):
                    print("papaya touch")
                    papayas_collected += 1
                    self.touchPapaya = True
"""