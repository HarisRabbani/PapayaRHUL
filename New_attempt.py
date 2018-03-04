from Vectors import Vector

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import time
import random

Img_user_Car = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/carUser.png')
#image enemy cars
Img_enemy_car_blue = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_blue.png')
Img_enemy_car_white=simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_white.jpg')
Img_enemy_car_cyan=simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_cyan.jpg')
Img_enemy_car_yellow=simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_yellow.jpg')
Img_enemy_car_green=simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Enemy_car_green.jpg')


img_cars_array=[Img_enemy_car_blue,Img_enemy_car_white,Img_enemy_car_cyan,Img_enemy_car_yellow,Img_enemy_car_green]

# x values should be updated and not y values by any +ve values
Img_top_tree = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Test_image.jpg')
Img_bottom_tree = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Test_image.jpg')
car_crash = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/carcrash.png')

display_width = 1000
display_height = 675

# car dimension
car_width = 140
car_height = 70
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

# Global variables
imgPos = [1000/2, 2*675/3.]
#imgPos=[250,250]
imgRot = 0



class User_Car:

    def __init__(self,pos):
        self.pos=pos
        self.vel=Vector()

    def draw(self,canvas):
        canvas.draw_image(Img_user_Car, IMG_CENTRE, IMG_DIMS, self.pos.getP(), IMG_DIMS)  # check codeskulptur for docs on parameter values


    def update(self):
        self.pos.add(self.vel)

        if (self.pos.x > display_width):
            self.pos.x = 0

            #dodged += 1  ##refers to number of times the track has been dodged through
            #score_game += 1
            #car_speed += 1 / 20  # accelarate


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

    def draw(self,canvas):
        #to sort out why the pic won't draw and the rest of the stuffs
        canvas.draw_line((0, 75), (display_width, 75), 12, 'Green')
        canvas.draw_line((0, 600), (display_width, 600), 12, 'Green')


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


    def keyDown(self, key):
        if key == simplegui.KEY_MAP['up']:
            self.up=True
        if key == simplegui.KEY_MAP['down']:
            self.down=True
        if key == simplegui.KEY_MAP['right']:
            self.right = True
        if key == simplegui.KEY_MAP['left']:
            self.left = True


    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['up']:
            self.up=False
        if key == simplegui.KEY_MAP['down']:
            self.down=False



class Interaction:
    #CRASH ADN THE OTHER BITS SHOULD BE DONE HERE
    def __init__(self,usr_car,kbd):
        self.user_car=usr_car
        self.keyboard=kbd


    def update(self):
        if self.keyboard.up and self.keyboard.right:
            self.user_car.vel.add(Vector((0.05, -0.05)))
        elif self.keyboard.down and self.keyboard.right:
            self.user_car.vel.add(Vector((0.05, 0.05)))
        elif  self.keyboard.left:
            self.user_car.vel.add(Vector((-0.05, 0)))
        elif self.keyboard.right:
            self.user_car.vel.add(Vector((0.05, 0)))
        else:
            self.user_car.vel=Vector((1,0))#if nothing is done then keep moving forward

#instances of all types, without brackets it points to a class but doesnt make an instance
object_User_Car= User_Car(Vector((75,random.randrange(150,550))))

#instead of using this the value should be bracketed to mean that it's a single arguement value

object_Enemy_Car=Enemy_Car(Vector((random.randrange(0,400),random.randrange(150,450))),Vector((3,0)),img_cars_array[random.randrange(0,5)])


object_Tree=TreeAndWall()

#object_interaction=interaction()

object_keyboard=keyboard()

object_interaction=Interaction(object_User_Car,object_keyboard)



#parameter passed in as canvas
def draw(canvas):
    object_interaction.update()
    object_Tree.draw(canvas)
    object_Tree.updateTree(canvas)
    object_Enemy_Car.draw(canvas)
    object_Enemy_Car.update()
    object_User_Car.draw(canvas)
    object_User_Car.update()






frame = simplegui.create_frame("A wheel", display_width, display_height)
frame.set_canvas_background('white')
#frame.set_mouseclick_handler(Game_instance.mouse)
frame.set_draw_handler(draw)#automatically passes on the canvas
frame.set_keydown_handler(object_keyboard.keyDown)
frame.set_keyup_handler(object_keyboard.keyUp)
frame.start()

