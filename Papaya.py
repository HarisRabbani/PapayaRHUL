from Vector import Vector
from Weapon import Weapon
from Wall import Wall
from WeaponCollision import WeaponCollision
from KeyboardClass import Keyboard
from Button import Button
from UserCar import UserCar
from Tree import Tree
from Sprite import Sprite
from Interaction import Interaction
from Interaction import Interaction
from Background import Background
from Obstacle import Obstacle
import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


DISPLAYW = 1000
DISPLAYH = 675

userCarImg = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/User_car_nitro.jpg')
#image enemy cars

papayaImg = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Papaya_image.jpg')
explosionSheet = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png')

# x values should be updated and not y values by any +ve values
treeImg = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Test_image.jpg')
car_crash = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/carcrash.png')
obstacle1img = simplegui.load_image("https://i.imgur.com/iHozk2k.png")
welcomeScreenButtonImg = simplegui.load_image("https://i.imgur.com/EuhSFX1.jpg")
welcomeScreenBG = simplegui.load_image("https://i.imgur.com/HEsDK8S.jpg")





explosionSprite = Sprite(explosionSheet, 9, 9)

userCar = UserCar(userCarImg, Vector((0, DISPLAYH/2)), 5, 5)
tree1 = Tree(treeImg, 0+treeImg.get_height()/2, DISPLAYW)
tree2 = Tree(treeImg, DISPLAYH-treeImg.get_height()/2, DISPLAYW)
w1 = Wall((0, 75), (DISPLAYW, 75), 12, 'Green', Vector((0, 1)))
w2 = Wall((0, 600), (DISPLAYW, 600), 12, 'Green', Vector((0, -1)))
bg = None
levelImage = ""
obstacle1 = Obstacle(Vector((240, DISPLAYH/2)), Vector((1, 0)), obstacle1img)
obstacle1.animate = True
kbd = Keyboard()

#interaction = Interaction(userCar, kbd)

def clickWelcomeScreen(pos):
    if welcomeScreenGo.contains(pos):
        welcomeScreenGo.clickBtn()

def drawWelcomeScreen(canvas):
    userCar.resetScore()
    canvas.draw_image(welcomeScreenBG, (welcomeScreenBG.get_width()/2, welcomeScreenBG.get_height()/2), (welcomeScreenBG.get_width(), welcomeScreenBG.get_height()), (DISPLAYW/2, DISPLAYH/2),(DISPLAYW, DISPLAYH))
    welcomeScreenGo.draw(canvas)

def click(pos):
    for x in range(0, len(arrayButton)):
        if arrayButton[x].contains(pos):
            print("button")
            arrayButton[x].clickBtn()

def draw(canvas):
    image = simplegui.load_image("https://i.imgur.com/8tYYDrc.png")
    canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (DISPLAYW/2,DISPLAYH/2), (image.get_width(), image.get_height()))
    for x in range(0, len(arrayButton)):
        arrayButton[x].draw(canvas)


def enter_game():
    frame.set_draw_handler(drawGame)

welcomeScreenGo = Button("https://i.imgur.com/EuhSFX1.jpg", (500, 500), enter_game)
interaction = Interaction(userCar, kbd, [tree1, tree2], w1, w2)

#parameter passed in as canvas
def drawGame(canvas):
    global papaya_time, tree_speed
    # global levelImage
    # image = simplegui.load_image(levelImage)
    # canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (display_width/2,display_height/2), (image.get_width(), image.get_height()))


   #obj_Int.CarsCollison()
    #obj_Int.TouchPapaya()
    #obj_Int.missileCollision()
    bg.update()
    obstacle1.update()
    bg.draw(canvas)
    interaction.update()
    tree1.update()
    tree2.update()
    userCar.update()
    tree1.draw(canvas)
    tree2.draw(canvas)
    userCar.draw(canvas)
    obstacle1.draw(canvas)
    w1.draw(canvas)
    w2.draw(canvas)
    interaction.weapColl.update()
    interaction.weapColl.draw(canvas)



#PUT LOGIC SOMEWHERE FOR BOOSTING
#if (papaya_time == True and obj_Int.touchPapaya == False):
#draw_Papaya(canvas)

   # if (interaction.carCollision == True):
    #    explosionSprite.draw(canvas, userCar.pos.x, userCar.pos.y)
     #   explosionSprite.animate = True

        #Logic to contain all explosions on screen and hiding what isn't being exploded.


def timer_handler():
   print("Papaya Spawn Stuff")


def draw_Papaya(canvas):
    pass
    #canvas.draw_image(papayaImg, (25, 25), (50, 50), (papaya_x, papaya_y), (50, 50))

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
    canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (DISPLAYW/2,DISPLAYH/2), (image.get_width(), image.get_height()))
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
    bgImage = simplegui.load_image("https://i.imgur.com/0uEOfSA.jpg")
    global bg
    bg = Background(bgImage, Vector((0, bgImage.get_height()/2)), DISPLAYW)
    trees = True
    interaction.passBack(bg)
    frame.set_mouseclick_handler(clickWelcomeScreen)
    frame.set_draw_handler(drawWelcomeScreen)

def enter_level2():
    bgImage = simplegui.load_image("https://i.imgur.com/1uBtqqe.jpg")
    global bg
    bg = Background(bgImage, Vector((bgImage.get_width()/2, bgImage.get_height()/2)), DISPLAYW)
    trees = True
    interaction.passBack(bg)
    frame.set_mouseclick_handler(clickWelcomeScreen)
    frame.set_draw_handler(drawWelcomeScreen)

def enter_level3():
    bgImage = simplegui.load_image("https://i.imgur.com/KzqV3D9.jpg")
    global bg
    bg = Background(bgImage, Vector((bgImage.get_width()/2, bgImage.get_height()/2)), DISPLAYW)
    trees = True
    interaction.passBack(bg)
    frame.set_mouseclick_handler(clickWelcomeScreen)
    frame.set_draw_handler(drawWelcomeScreen)


start = Button("https://i.imgur.com/xoZnCmL.png", (120, 450), enter_level_select)
help = Button("https://i.imgur.com/6OfeKop.png", (470, 450), enter_help)
quit = Button("https://i.imgur.com/zSSFt11.png", (820,450), quit)
arrayButton = [start, help, quit]
frame = simplegui.create_frame("Papaya Racers", DISPLAYW, DISPLAYH)
frame.set_mouseclick_handler(clickMainMenu)

frame.set_draw_handler(draw)#automatically passes on the canvas
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
timer = simplegui.create_timer(5000, timer_handler)
timer.start()
frame.start()
