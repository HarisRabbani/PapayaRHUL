#from SpriteSheet import Spritesheet here when this is called, it will run first
from Vector import Vector
from Weapon import Weapon
from Wall import Wall
from WeaponCollision import WeaponCollision
try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import time
import random
import math

Img_user_Car = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/carUserNewPic.png')
#image enemy cars
Img_enemy_car_blue = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_blue.png')
Img_enemy_car_white=simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_white.jpg')
Img_enemy_car_cyan=simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_cyan.jpg')
Img_enemy_car_yellow=simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_yellow.jpg')
Img_enemy_car_green=simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_green.jpg')

Img_papaya= simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Papaya_image.jpg')
img_cars_array=[Img_enemy_car_blue,Img_enemy_car_white,Img_enemy_car_cyan,Img_enemy_car_yellow,Img_enemy_car_green]

# x values should be updated and not y values by any +ve values
Img_top_tree = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Test_image.jpg')
Img_bottom_tree = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Test_image.jpg')
car_crash = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/carcrash.png')

display_width = 1000
display_height = 675

# car dimension
car_width = 140
car_height = 65
car_speed=3

car_x = 5
car_y = (display_height * 0.65)

tree_w = 605
tree_h=57
tree_speed = 7
tree_y_top=10
tree_y_bottom=700


IMG_CENTRE = (70, 35)
IMG_DIMS = (140,70)

STEP =0.5

papaya_x=0
papaya_y=0
papaya_size=50
papaya_time=False
papayas_collected=0

rockets = []
walls = []
weapCollision = WeaponCollision()

# Global variables
imgPos = [1000/2, 2*675/3.]
#imgPos=[250,250]
imgRot = 0



class User_Car:

    def __init__(self,pos):
        self.pos=pos
        self.vel=Vector()
        self.dodged=0
        self.score=0
        self.heading = self.vel  # Set a variable which represents the heading vector to use as a dot product
        self.rotating = True
        self.rotation = 0  # Radians needed
        # Car physics code





    def draw(self,canvas):
        canvas.draw_image(Img_user_Car, IMG_CENTRE, IMG_DIMS, self.pos.getP(), IMG_DIMS, self.rotation)  # check codeskulptur for docs on parameter values
        canvas.draw_text('Speed: (' +str(self.vel.x)+' , '+str(self.vel.y)+') px/s' , (20, 13), 15, 'Black')
        canvas.draw_text('Dodged: ' + str(self.dodged), [20, 30],15, 'Black')
        canvas.draw_text('Papayas: '+str(papayas_collected), (20, 45), 15, 'Black')
        canvas.draw_text('Final Score: '+str(self.score), (20, 62), 18, 'Black')

    def update(self):




        self.pos.add(self.vel)


        if (self.pos.x > display_width):
            self.pos.x = 0
            self.dodged += 1
            self.score+=1 + papayas_collected
            #car_speed += 1 / 20  # accelarate

    def Collisonwall(self):

        if (self.pos.y<75+car_height or self.pos.y+car_height>600):
            return True
        else:
            return False




    def rotator(self, direction):
        if not direction:
            self.rotation -= 1 / 180


        if direction:
            self.rotation += 1 / 180





class Enemy_Car:

    def __init__(self,pos,vel,img):
        self.pos = pos
        self.vel = vel
        self.img=img

    def draw(self, canvas):
        canvas.draw_image(self.img, IMG_CENTRE, IMG_DIMS,self.pos.getP(),IMG_DIMS)  # check codeskulptur for docs on parameter values

    def update(self):
        self.pos.add(self.vel)
        if (self.pos.x > display_width):
            self.pos.x=0-car_width
            self.pos.y = random.randrange(100,550)


class TreeAndWall:

    global Img_top_tree
    global weapCollision
    w1 = Wall((0, 75), (display_width, 75), 12, 'Green', Vector((0, 1)))
    w2 = Wall((0, 600), (display_width, 600), 12, 'Green', Vector((0, -1)))

    weapCollision.addWall(w1)
    weapCollision.addWall(w2)


    def draw(self,canvas):
        #to sort out why the pic won't draw and the rest of the stuffs
        # canvas.draw_line((0, 75), (display_width, 75), 12, 'Green')
         # canvas.draw_line((0, 600), (display_width, 600), 12, 'Green')
        pass

    def updateTree(self,canvas):
        global tree_y_top
        global tree_y_bottom
     #  global car_speed  and values cannot be hanged unless it's inherited as a global value

        tree_y_top-=tree_speed
        tree_y_bottom-=tree_speed

        if tree_y_top < 0-tree_w:
            tree_y_top = display_width + tree_w  # reset y
            #car_speed += 1 / 15

        if tree_y_bottom < 0-tree_w:
            tree_y_bottom = display_width + tree_w  # reset y
            #car_speed += 1 / 15


        canvas.draw_image(Img_top_tree, (302, 28), (605, 57), (tree_y_top, 28), (400, 70))  # 605x57
        canvas.draw_image(Img_bottom_tree, (302, 28), (605, 57), (tree_y_bottom, 641), (400, 68))  # 605x57


class keyboard:

    def __init__(self):
        self.right = False
        self.left = False
        self.up=False
        self.down=False
        self.space = False


    def keyDown(self, key):
        if key == simplegui.KEY_MAP['up']:
            self.up=True
        if key == simplegui.KEY_MAP['down']:
            self.down=True
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True
        if key == simplegui.KEY_MAP['space']:
            self.space = True


    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up=False
        if key == simplegui.KEY_MAP['down']:
            self.down=False
        if key == simplegui.KEY_MAP['space']:
            self.space = False


class Interaction:
    #CRASH ADN THE OTHER BITS SHOULD BE DONE HERE
    def __init__(self,usr_car,kbd):
        self.user_car=usr_car
        self.keyboard=kbd
        self.carCollision=False
        self.touchPapaya=False

    def update(self):
       if not obj_user_car.Collisonwall():
            if self.keyboard.up:
                #self.user_car.vel.add(Vector((0.05, -0.05)))
                self.user_car.rotator(False)
                self.user_car.rotating = True

            elif self.keyboard.down:
                #self.user_car.vel.add(Vector((0.05, 0.05)))
                self.user_car.rotator(True)
                self.user_car.rotating = True

            elif  self.keyboard.left:
                self.user_car.vel.add(Vector((-0.05, 0)))
            elif self.keyboard.right:
                self.user_car.vel.add(Vector((0.05, 0)))
            elif self.keyboard.space:
                url = 'https://i.imgur.com/RVi7F76.png'
                missile = Weapon(Vector((obj_user_car.pos.x + IMG_DIMS[0], obj_user_car.pos.y)), obj_user_car.vel.copy().normalize(), url, 4, 4)
                weapCollision.addWeapon(missile)
            else:
                self.user_car.vel=Vector((1,0))#if nothing is done then keep moving forward
                pass

       else:
           #call game crash
           #then game over interface
            obj_spriteS.collision=True


    def CarsCollison(self):

        """
        #car to enemy (x)
        #enemy to car (x)
        #car to enemy - top to bottom crash
        #car to enemy - bototm to top crash
        """

        ##To be improved
        if (obj_user_car.pos.x +car_width >(obj_Enemey_car.pos.x) and obj_user_car.pos.x <obj_Enemey_car.pos.x +car_width) \
                or (obj_Enemey_car.pos.x+car_width>obj_user_car.pos.x and obj_Enemey_car.pos.x < obj_user_car.pos.x+car_width):
            if (obj_user_car.pos.y+car_height>obj_Enemey_car.pos.y and obj_user_car.pos.y<obj_Enemey_car.pos.y+car_height) \
                    or (obj_user_car.pos.y<obj_Enemey_car.pos.y+car_height and obj_Enemey_car.pos.y>obj_user_car.pos.y):
                print("collison detected")
                self.carCollision=True

    def TouchPapaya(self):
        global papaya_y
        global papaya_x
        global papayas_collected

        if (self.touchPapaya)==False:
            if ((obj_user_car.pos.x +car_width >papaya_x) and obj_user_car.pos.x <papaya_x +papaya_size):
                if (papaya_y<obj_user_car.pos.y and papaya_y+papaya_size<obj_user_car.pos.y) or \
                (obj_user_car.pos.y<papaya_y+papaya_size) and (obj_user_car.pos.y<papaya_y):
                    print("papaya touch")
                    papayas_collected+=1
                    self.touchPapaya=True


class Spritesheet:
   def __init__(self):
       self.img = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png')
       self.width = 400
       self.height = 400
       self.rows = 9
       self.columns = 9
       self.frameWidth = 100
       self.frameHeight = 100
       self.frameCentreX = self.frameWidth / 2
       self.frameCentreY = self.frameHeight / 2
       self.dimX = 100
       self.dimY = 100
       self.frameIndex = [9, 9]  # maximum value
       self.newPos = (0,0)#Default value
       self.collision=False

   # canvas.draw_image(image, center_source, width_height_source, center_dest, width_height_dest, rotation)
   def draw(self, canvas,posX,posY):
       canvas.draw_image(self.img,
                         (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                          self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                         (self.frameWidth, self.frameHeight),
                         ((posX,posY)),
                         (self.dimX, self.dimY))

   def nextFrame(self):  # value can be passed to change the animation stating point
       # refers to the current frame index(assigning a value to it initially)
       self.frameIndex[0] = (self.frameIndex[0] + 1) % self.columns
       if self.frameIndex[0] == 0:
           self.frameIndex[1] = (self.frameIndex[1] + 1) % self.rows  # y is referred to by the rows





class Button:

    def __init__(self, image, pos, trigger):
        self.image = simplegui.load_image(image)
        self.pos = pos
        self.trigger = trigger
        self.clicked = False

    def draw(self, canvas):
        canvas.draw_image(self.image, (self.image.get_width() / 2, self.image.get_height() / 2),(self.image.get_width(), self.image.get_height()), self.pos,(self.image.get_width(), self.image.get_height()))

    def contains(self, pos):
        return pos[0] > self.pos[0] - (self.image.get_width() / 2) and pos[0] < self.pos[0] + (self.image.get_width() / 2) and pos[1] > self.pos[1] - (self.image.get_height() / 2) and pos[1] < self.pos[1] + (self.image.get_height() / 2)

    def clickBtn(self):
        self.clicked = True
        self.trigger()




# instead of using this the value should be bracketed to mean that it's a single arguement value
#instances of all types, without brackets it points to a class but doesnt make an instance

obj_user_car= User_Car(Vector((75,random.randrange(150,530))))

obj_Enemey_car=Enemy_Car(Vector((random.randrange(0,400),random.randrange(150,450))),Vector((3,0)),img_cars_array[random.randrange(0,5)])


obj_Tree=TreeAndWall()

obj_Kbd=keyboard()

obj_Int=Interaction(obj_user_car,obj_Kbd)

obj_spriteS=Spritesheet()

def click(pos):
    for x in range(0, len(arrayButton)):
        if(arrayButton[x].contains(pos)):
            print("button")
            arrayButton[x].clickBtn()

def draw(canvas):
    image = simplegui.load_image("https://i.imgur.com/8tYYDrc.png")
    canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (display_width/2,display_height/2), (image.get_width(), image.get_height()))
    for x in range(0, len(arrayButton)):
        arrayButton[x].draw(canvas)




def enter_game():
    frame.set_draw_handler(drawGame)

#parameter passed in as canvas
def drawGame(canvas):
    global papaya_time
    # global levelImage
    # image = simplegui.load_image(levelImage)
    # canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (display_width/2,display_height/2), (image.get_width(), image.get_height()))

    obj_Int.update()
    obj_Tree.draw(canvas)
    obj_Tree.updateTree(canvas)
    obj_Enemey_car.draw(canvas)
    obj_Enemey_car.update()
    obj_user_car.draw(canvas)
    obj_user_car.update()
    obj_Int.CarsCollison()
    obj_Int.TouchPapaya()

    weapCollision.draw(canvas)


    if (papaya_time == True and obj_Int.touchPapaya == False):
        draw_Papaya(canvas)

    if (obj_Int.carCollision == True):
        obj_spriteS.draw(canvas, obj_user_car.pos.x, obj_user_car.pos.y)
        obj_spriteS.nextFrame()

    if (obj_spriteS.collision == True):
        obj_spriteS.draw(canvas, obj_user_car.pos.x, obj_user_car.pos.y)
        obj_spriteS.nextFrame()



def timer_handler():
    global papaya_y
    global papaya_x
    global papaya_time
    papaya_time=True
    obj_Int.touchPapaya=False #value set back to false, so that papaya can respawn if collected
    papaya_x = random.randrange(150, 950)
    papaya_y = random.randrange(100, 550)


def draw_Papaya(canvas):
    canvas.draw_image(Img_papaya, (25, 25), (50, 50), (papaya_x, papaya_y), (50, 50))

def clickMainMenu(pos):
    for x in range(0, len(arrayButton)):
        if(arrayButton[x].contains(pos)):
            arrayButton[x].clicked = True
            arrayButton[x].clickBtn()

def clickLevelSelect(pos):
    for x in range(0, len(levelButton)):
        if(levelButton[x].contains(pos)):
            levelButton[x].clickBtn()

def enter_help():
    pass

def level_select(canvas):
    image = simplegui.load_image("https://i.imgur.com/8tYYDrc.png")
    canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (display_width/2,display_height/2), (image.get_width(), image.get_height()))
    level1 = Button("https://i.imgur.com/sZlcBI9.png", (150, 450), enter_level1)
    level2 = Button("https://i.imgur.com/VWL7wfu.png", (500, 450), enter_level2)
    level3 = Button("https://i.imgur.com/wVUdTVL.png", (850, 450), enter_level3)
    global levelButton
    levelButton = [level1, level2, level3]
    for x in range(0, len(levelButton)):
        levelButton[x].draw(canvas)

def enter_level_select():
    frame.set_mouseclick_handler(clickLevelSelect)
    frame.set_draw_handler(level_select)

def quit():
    exit(0)

def enter_level1():
    # levelImage = ""
    frame.set_draw_handler(drawGame)

def enter_level2():
    # levelImage = ""
    frame.set_draw_handler(drawGame)

def enter_level3():
    # levelImage = ""
    frame.set_draw_handler(drawGame)

start = Button("https://i.imgur.com/xoZnCmL.png", (120, 450), enter_level_select)
help = Button("https://i.imgur.com/6OfeKop.png", (470, 450), enter_help)
quit = Button("https://i.imgur.com/zSSFt11.png", (820,450), quit)
arrayButton = [start, help, quit]
frame = simplegui.create_frame("A wheel", display_width, display_height)
frame.set_mouseclick_handler(clickMainMenu)
frame.set_canvas_background('white')
frame.set_draw_handler(draw)#automatically passes on the canvas
frame.set_keydown_handler(obj_Kbd.keyDown)
frame.set_keyup_handler(obj_Kbd.keyUp)
timer = simplegui.create_timer(5000, timer_handler)
timer.start()
frame.start()

