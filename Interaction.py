# Class to hold all of the logic for collisions, add things to the constructor and add the logic.
from Vector import Vector
from UserCar import UserCar
from Weapon import Weapon
from WeaponCollision import WeaponCollision

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import random

class Interaction:

    def __init__(self, usr_car, kbd, trees, w1, w2):
        self.uCar = usr_car
        self.w1 = w1
        self.w2 = w2
        self.trees = trees
        self.kbd = kbd
        self.carCollision = False
        self.missileCollide = False
        self.touchPapaya = False
        self.offScreen = False  # WHEN TRUE - GAME SHOULD END
        self.weapColl = WeaponCollision()
        self.weapColl.addWall(w1)
        self.weapColl.addWall(w2)


    def update(self):
        # Check for wall collision first
            if self.kbd.up:
                self.uCar.rotator(False)
            if self.kbd.down:
                self.uCar.rotator(True)

            if self.kbd.right:
                if self.uCar.vel.length() > 10:
                    pass
                else:
                   # self.uCar.vel.add(Vector((0.05, 0)))
                    self.uCar.animate = True
                    for i in self.trees:
                        i.vel.sub(Vector((0.05, 0)))
            else:
                self.uCar.animate = False

            if self.kbd.left:
              #  self.uCar.vel.add(Vector((-0.05, 0)))
                for i in self.trees:
                    i.vel.add(Vector((0.05, 0)))
            if self.kbd.space:
                image = simplegui.load_image('https://i.imgur.com/RVi7F76.png')
                missile = Weapon(Vector((self.uCar.pos.x + self.uCar.frameWidth/2, self.uCar.pos.y)), Vector((5, self.uCar.vel.y)), image, 4, 4)
                self.weapColl.addWeapon(missile)


            # For all userCar corners and offsets. Check with all other ones.
            for i in self.uCar.corners:
                for j in self.uCar.offsets:
                    if i.y < 75 + self.w1.border or j.y < 75 + self.w1.border:
                        self.offScreen = True
                    if i.y > 600 - self.w1.border or j.y > 600 - self.w1.border:
                        self.offScreen = True






            
           

        # else:
        # call game crash
        # then game over interface
        # obj_explosion_spriteS=True




