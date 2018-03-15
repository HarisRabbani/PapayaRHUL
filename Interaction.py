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

    def __init__(self, usr_car, kbd, trees, w1, w2, obs):
        self.canvW = 1000
        self.uCar = usr_car
        self.w1 = w1
        self.bg = None
        self.obstacles = obs
        self.w2 = w2
        self.trees = trees
        self.kbd = kbd
        self.carCollision = False
        self.missileCollide = False
        self.touchPapaya = False
        self.offScreen = False  # WHEN TRUE - GAME SHOULD END
        self.weapons = []
        self.walls = [w1, w2]
        self.inCollision = False

    def passBack(self, bg):
        self.bg = bg

    def draw(self, canvas):
        for i in self.weapons:
            i.update()
            i.draw(canvas)

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
                self.bg.vel.sub(Vector((0.05, 0)))
                for i in self.trees:
                    i.vel.sub(Vector((0.05, 0)))
        else:
            self.uCar.animate = False

        if self.kbd.left:
            #  self.uCar.vel.add(Vector((-0.05, 0)))
            self.bg.vel.add(Vector((0.05, 0)))
            for i in self.trees:
                i.vel.add(Vector((0.05, 0)))
        if self.kbd.space:
            image = simplegui.load_image('https://i.imgur.com/RVi7F76.png')
            missile = Weapon(Vector((self.uCar.pos.x + self.uCar.frameWidth / 2, self.uCar.pos.y)),
                             Vector((5, self.uCar.vel.y)), image, 4, 4)
            self.weapons.append(missile)

        # For all userCar corners and offsets. Check with all other ones.
        for i in self.uCar.corners:
            for j in self.uCar.offsets:
                if i.y < 75 + self.w1.border or j.y < 75 + self.w1.border:
                    self.uCar.lives = 0
                    print("Car hitting top wall")
                if i.y > 600 - self.w2.border or j.y > 600 - self.w2.border:
                    self.uCar.lives = 0
                    print("Car hitting bottom wall")
                # For every obstacle

                for v in self.obstacles:
                    if i.x > v.offL.x and i.x < v.offR.x or j.x > v.offL.x and j.x < v.offR.x:
                        if i.y > v.offT.y and i.y < v.offB.y or j.y > v.offT.y and j.y < v.offB.y:
                            self.uCar.lives -= 1  # Register car hit with
                            v.animate = True
                            print("Car hitting obstacle")

        for x in self.weapons:
            if x.pos.x > self.canvW or x.frameElapsed > x.row*x.column:  # Remove if gone off or animated once.
                self.weapons.remove(x)


            for i in x.corners:
                for j in x.offsets:

                    if i.y < 75 + self.w1.border or j.y < 75 + self.w1.border:
                        if self.inCollision == False:
                            x.animate = True
                            print("Rocket hitting top wall")

                            self.inCollision = True

                    else:
                        self.inCollision = False

                    if i.y > 600 - self.w1.border or j.y > 600 - self.w1.border:
                        if not self.inCollision:
                            x.animate = True
                            print("Rocket hitting bottom wall")
                            self.inCollision = True
                    else:
                        self.inCollision = False

                    for v in self.obstacles:
                        if i.x > v.offL.x and i.x < v.offR.x or j.x > v.offL.x and j.x < v.offR.x:
                            if i.y > v.offT.y and i.y < v.offB.y or j.y > v.offT.y and j.y < v.offB.y:
                                print(" Rocket - Obstacle hit")
                                self.obstacles.remove(v)
                                x.animate = True




        # Check Car collision with obstacle objects.

    # else:
    # call game crash
    # then game over interface
    # obj_explosion_spriteS=True
