# Class to hold all of the logic for collisions, add things to the constructor and add the logic.
from Vector import Vector
from UserCar import UserCar
from Weapon import Weapon
import random

class Interaction:

    def __init__(self, usr_car, kbd):
        self.user_car = usr_car
        self.keyboard = kbd
        self.carCollision = False
        self.missileCollide = False
        self.touchPapaya = False

    def update(self):
        # Check for wall collision first
            if self.keyboard.up:
                # self.user_car.vel.add(Vector((0.05, -0.05)))
                self.user_car.rotator(False)
                # self.user_car.rotating = True

            elif self.keyboard.down:
                # self.user_car.vel.add(Vector((0.05, 0.05)))
                self.user_car.rotator(True)
                # self.user_car.rotating = True

            elif self.keyboard.left:
                self.user_car.vel.add(Vector((-0.05, 0)))
            elif self.keyboard.right:  # if the right is pressed then add the nitro animation
                if self.user_car.vel.length() > 10:
                    pass
                else:
                    self.user_car.vel.add(Vector((0.05, 0)))
            elif self.keyboard.space:

                url = 'https://i.imgur.com/RVi7F76.png'
                #missile = Weapon(Vector((self.user_car.pos.x + self.user_car., self.user_car.pos.y)),
                 #                Vector(((random.randrange(2, 5)), 0)), url, 4, 4)


                # obj_missile = Weapon(Vector((self.user_car.pos.x + IMG_usr_DIMS[0], self.user_car.pos.y)),Vector((random.randrange(1, 5), 0)), missile_url, 4, 4)
                # weapCollision.addWeapon(obj_missile)
            else:
                # self.user_car.vel=Vector((1,0))#if nothing is done then keep moving forward
                pass

        # else:
        # call game crash
        # then game over interface
        # obj_explosion_spriteS=True




