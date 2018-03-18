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

    def __init__(self, usr_car, usrCar2, kbd, trees, w1, w2, obs, twoPlayer):
        self.canvW = 1000
        self.uCar = usr_car
        self.uCar2 = usrCar2
        self.twoPlayer = twoPlayer
        if twoPlayer:
            self.cars = [self.uCar, self.uCar2]
        else:
            self.cars = [self.uCar]
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
        self.firingCount = 0
        self.firingCount2 = 0

    def passBack(self, bg):
        self.bg = bg

    def draw(self, canvas):
        for i in self.weapons:
            i.update()
            i.draw(canvas)

    def removeLife(self, car):
        self.bg.vel = Vector((-1, 0))
        for i in self.trees:
            i.vel = Vector((-1, 0))
        if car.c_health_status == 3:
            car.c_health_status = 2
        elif car.c_health_status == 2:
            car.c_health_status = 1
        elif car.c_health_status == 1:
            car.c_health_status = 0


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
            if self.firingCount >= 1:
                pass
            else:
                image = simplegui.load_image('https://i.imgur.com/RVi7F76.png')
                missile = Weapon(Vector((self.uCar.pos.x + self.uCar.frameWidth / 2, self.uCar.pos.y)),
                                 Vector((5, self.uCar.vel.y)), image, 4, 4)
                self.weapons.append(missile)
                self.firingCount += 1
        else:
            self.firingCount = 0

        if self.twoPlayer:
            if self.kbd.w:
                self.uCar2.rotator(False)
            if self.kbd.s:
                self.uCar2.rotator(True)

            if self.kbd.d:
                if self.uCar2.vel.length() > 10:
                    pass
                else:
                    # self.uCar2.vel.add(Vector((0.05, 0)))
                    self.uCar2.animate = True
                    self.bg.vel.sub(Vector((0.05, 0)))
                    for i in self.trees:
                        i.vel.sub(Vector((0.05, 0)))
            else:
                self.uCar2.animate = False

            if self.kbd.a:
                #  self.uCar2.vel.add(Vector((-0.05, 0)))
                self.bg.vel.add(Vector((0.05, 0)))
                for i in self.trees:
                    i.vel.add(Vector((0.05, 0)))

            if self.kbd.f:
                if self.firingCount2 >= 1:
                    pass
                else:
                    image = simplegui.load_image('https://i.imgur.com/RVi7F76.png')
                    missile = Weapon(Vector((self.uCar2.pos.x + self.uCar2.frameWidth / 2, self.uCar2.pos.y)),
                                 Vector((5, self.uCar2.vel.y)), image, 4, 4)
                    self.weapons.append(missile)
                    self.firingCount2 += 1
            else:
                self.firingCount2 = 0

        # For all userCar corners and offsets. Check with all other ones.
        for x in self.cars:
            for i in x.corners:
                for j in x.offsets:
                    if i.y < 75 + self.w1.border or j.y < 75 + self.w1.border:

                        # x.lives = 0
                        x.pos = Vector((50, 337))
                        self.removeLife(x)

                        x.update()
                        break

                        # print("Car hitting top wall")

                    if i.y > 600 - self.w2.border and j.y > 600 - self.w2.border:
                        # x.lives = 0

                        x.pos = Vector((50, 675 / 2))
                        # break

                        self.removeLife(x)

                        x.update()
                        break
                        # print("Car hitting bottom wall")

                    # For every obstacle

                for v in self.obstacles:
                    if i.x > v.offL.x and i.x < v.offR.x or j.x > v.offL.x and j.x < v.offR.x:
                        if i.y > v.offT.y and i.y < v.offB.y or j.y > v.offT.y and j.y < v.offB.y:
                            self.removeLife(x)  # Register car hit with
                            self.obstacles.remove(v)
                            x.update()
                            v.animate = True
                            print("Car hitting obstacle")

        for x in self.weapons:
            if x.pos.x > self.canvW or x.frameElapsed > x.row * x.column:  # Remove if gone off or animated once.
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
