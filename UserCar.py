from Vector import Vector
from Sprite import Sprite

class UserCar(Sprite):

#user's health will be updated below
#we will need to have a current variable which keeps track of user's health

    def __init__(self, image, pos, row, column, health0, health1, health2, health3, playerNum):
        super().__init__(image, row, column, pos)
        self.pos = pos
        self.pos.x = self.pos.x + self.frameWidth/2
        super().defineOffsets(pos)
        super().defineCorners(pos)
        self.vel = Vector((5, 0))
        self.heading = self.vel  # Set a variable which represents the heading vector to use as a dot product
        self.rotating = True
        self.rotation = 0  # Radians needed
        self.papayaCollected = 0
        self.imgDim = [self.img.get_width(), self.img.get_height()]
        self.lives = 3
        self.img_health_0 = health0
        self.img_health_1 = health1
        self.img_health_2 = health2
        self.img_health_3 = health3
        self.c_health_status = 3
        self.health_img = self.img_health_3
        self.playerNum = playerNum
        self.name = "Player " + str(playerNum)
        # Car physics code

    def draw(self, canvas):
        canvas.draw_image(self.img, (self.x, self.y), (self.frameWidth, self.frameHeight), self.pos.getP(), [self.frameWidth, self.frameHeight], self.rotation)  # check codeskulptur for docs on parameter values
        if self.playerNum == 2:
            canvas.draw_text('Player 2 Papaya: ' + str(self.papayaCollected), (20, 45), 15, 'Black')
            canvas.draw_image(self.health_img, (75 / 2, 30 / 2), (75, 30), (500, 50), (75, 30))  # hard coded values
        else:
            canvas.draw_text('PLayer 1 papaya: ' + str(self.papayaCollected), (20, 10), 15, 'Black')
            canvas.draw_image(self.health_img, (75 / 2, 30 / 2), (75, 30), (200, 50), (75, 30))  # hard coded values


    def reset(self):

        self.papayaCollected = 0
        self.c_health_status = 3
        self.health_img = self.img_health_3
        self.pos = Vector((0 + self.frameWidth / 2, 1000 * 0.25))
        self.vel = Vector((5, 0))
        self.rotation = 0
        self.update()



    def update(self):
        if (self.animate == False) or (self.update_x() and self.update_y()):
            self.frameIndex[0] = 0
            self.frameIndex[1] = 0
            self.update_x()
            self.update_y()
        super(UserCar, self).update()
        self.pos.y += self.vel.y
        super().defineOffsets(self.pos)
        super().defineCorners(self.pos)

        #Score is increased by other factors too.



        if (self.c_health_status == 2):#hard coded values
            self.health_img=self.img_health_2
        elif (self.c_health_status == 1):
            self.health_img = self.img_health_1
        elif (self.c_health_status == 0):
            self.health_img = self.img_health_0

    def Collisonwall(self):
        #REDO THIS CODE, CAR SHOULD BE ADDED TO INTERACTION
        if self.pos.y < 75 + self.imgDim[1] or self.pos.y + self.imgDim[1] > 600:
            return True
        else:
            return False

    def rotator(self, direction):  # Direction is a boolean which represents which way should be turned
        if not direction:
            if self.rotation < -0.5:
                pass
            else:
                self.rotation -= 1 / 180 * 5
                self.vel.rotateRad(-1 / 180 * 5)

        if direction:
            if self.rotation > 0.5:
                pass
            else:
                self.rotation += 1 / 180 * 5
                self.vel.rotateRad(1 / 180 * 5)
