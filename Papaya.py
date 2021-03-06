from Vector import Vector
from Wall import Wall
from KeyboardClass import Keyboard
from Button import Button
from UserCar import UserCar
from Tree import Tree
from Interaction import Interaction
from Background import Background
from Obstacle import Obstacle
from PapayaPick import PapayaPick
from BombClass import Bomb
import random

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import math
import random

# The main class - AKA THE GAME class. This is where all the game logic is held.

DISPLAYW = 1000
DISPLAYH = 675

userCarImg = simplegui.load_image('https://i.imgur.com/uB67l2f.png')
user2img = simplegui.load_image("https://i.imgur.com/Zgkwn3T.png")
papayaImg = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Papaya_image.jpg')
explosionSheet = simplegui.load_image('http://www.cs.rhul.ac.uk/courses/CS1830/sprites/explosion-spritesheet.png')
car_crash = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/carcrash.png')
welcomeScreenButtonImg = simplegui.load_image("https://i.imgur.com/EuhSFX1.jpg")
welcomeScreenBG = simplegui.load_image("https://i.imgur.com/kpqKIoh.png")
obstacle1img = simplegui.load_image("https://i.imgur.com/waPEQMH.png")
obstacle2img = simplegui.load_image("https://i.imgur.com/8HA81OA.png")
OBS = [obstacle1img, obstacle2img]
rowCols = [(3, 3), (2, 4)]

#health images
health_0 = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Health_0.png')
health_1 = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Health_1.png')
health_2 = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Health_2.png')
health_3 = simplegui.load_image('http://personal.rhul.ac.uk/zeac/084/Health_3.png')
global twoPlayer
twoPlayer = False
userCar = UserCar(userCarImg, Vector((0, DISPLAYH*0.25)), 5, 5,health_0,health_1,health_2,health_3, 1)
userCar2 = UserCar(user2img, Vector((0, DISPLAYH*0.75)), 5, 5,health_0,health_1,health_2,health_3, 2)
w1 = Wall((0, 75), (DISPLAYW, 75), 12, 'Green', Vector((0, 1)))
w2 = Wall((0, 600), (DISPLAYW, 600), 12, 'Green', Vector((0, -1)))
bg = None
bombs = []
levelImage = ""
obstacles = []
papaya = []
score = 0
timeElapsed = 0
frameElapsed = 0
kbd = Keyboard()
global treeImg
treeImg = None
tree1 = None
tree2 = None
interaction = None


def click(pos):
    for x in range(0, len(arrayButton)):
        if arrayButton[x].contains(pos):
            arrayButton[x].clickBtn()


def draw(canvas):
    image = simplegui.load_image("https://i.imgur.com/8tYYDrc.png")
    canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (DISPLAYW/2,DISPLAYH/2), (image.get_width(), image.get_height()))
    for x in range(0, len(arrayButton)):
        arrayButton[x].draw(canvas)


def twoPlayers():
    global interaction, twoPlayer
    #interaction = Interaction(userCar, userCar2, kbd, [tree1, tree2], w1, w2, obstacles,bombs,papaya ,True)
    twoPlayer = True
    enter_level_select()


def onePlayers():
    global interaction, twoPlayer
    #interaction = Interaction(userCar, userCar2, kbd, [tree1, tree2], w1, w2, obstacles,bombs,papaya, False)
    twoPlayer = False
    enter_level_select()


def clickPlayerSelect(pos):
    for x in range(0, len(playerButton)):
        if playerButton[x].contains(pos):
            playerButton[x].clickBtn()

def drawPlayerSelect(canvas):
    image = simplegui.load_image("https://i.imgur.com/8tYYDrc.png")
    canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (DISPLAYW/2,DISPLAYH/2), (image.get_width(), image.get_height()))
    for x in range(0, len(playerButton)):
        playerButton[x].draw(canvas)


def clickWelcomeScreen(pos):
    if welcomeScreenGo.contains(pos):
        welcomeScreenGo.clickBtn()

def enterWelcomeScreen():
    frame.set_mouseclick_handler(clickWelcomeScreen)
    frame.set_draw_handler(drawWelcomeScreen)

def clickGameOver(pos):
    for x in range(0, len(gameOverButtons)):
        if gameOverButtons[x].contains(pos):
            gameOverButtons[x].clickBtn()

def drawGameOver(canvas):
    image = simplegui.load_image("https://i.imgur.com/rvvHZnj.png")
    canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (DISPLAYW/2,DISPLAYH/2), (image.get_width(), image.get_height()))
    canvas.draw_text("Final Score: " + str(finalScore), (DISPLAYW/2-100, 350), 18, "Black", "monospace")
    canvas.draw_text("Total Papayas: " + str(papayaCollectedTotal), (DISPLAYW/2-100, 300), 18, "Black", "monospace")
    canvas.draw_text("Final Time: " + str(finalTime), (DISPLAYW/2-100, 400), 18, "Black", "monospace")
    for x in range(0, len(gameOverButtons)):
        gameOverButtons[x].draw(canvas)

def gameOver():
    stopTimers()
    engine.pause()
    engine.rewind()
    # STOP UPDATING EVERYTHING HERE
    reset()
    global finalScore
    finalScore = (userCar.papayaCollected + userCar2.papayaCollected) * score
    global finalTime
    finalTime = timeElapsed
    global papayaCollectedTotal
    papayaCollectedTotal = userCar.papayaCollected
    if interaction.twoPlayer:
        papayaCollectedTotal += userCar2.papayaCollected
    frame.set_mouseclick_handler(clickGameOver)
    frame.set_draw_handler(drawGameOver)

    # Display Score, final score, display time elapsed etc, display papaya picked.


def reset(): # Method to reset all the variables so that the user can restart the game
    for i in obstacles:
        obstacles.remove(i)

    for b in bombs:
        bombs.remove(b)
    global score, userCar, userCar2, timeElapsed
    score = 0
    timeElapsed = 0
    userCar.reset()
    userCar2.reset()



def drawText(canvas):
    print("here")
    canvas.draw_text("Score: " + str(score), (DISPLAYW/2, 15), 18, "Black", "monospace")
    canvas.draw_text("Speed: " + str(abs(tree1.vel.x)), (DISPLAYW/2, 30), 18, "Black", "monospace")
    canvas.draw_text("Time elapsed: " + str(timeElapsed) + " s", (DISPLAYW/2, 50), 18, "Black", "monospace")


def drawAllElements(canvas):

    bg.draw(canvas)
    tree1.draw(canvas)
    tree2.draw(canvas)
    w1.draw(canvas)
    w2.draw(canvas)
    interaction.draw(canvas)
    #Papaya.draw(canvas)
    userCar.draw(canvas)
    if interaction.explosion:
        pass #  Draw explosion here
    if interaction.twoPlayer:
        userCar2.draw(canvas)
    drawText(canvas)

def updateAllElements(canvas):
    global frameElapsed, timeElapsed, score
    frameElapsed += 1
    score += 1
    if frameElapsed % 60 == 0:
        timeElapsed += 1

    engine.play()
    bg.update()
    interaction.update()
    tree1.update()
    tree2.update()
    userCar.update()
    if interaction.explosion:
        pass #  Update Explosion here
    if interaction.twoPlayer:
        userCar2.update()
    interaction.update()
    #Papaya.update()
    if interaction.twoPlayer and (userCar.c_health_status==0 and userCar2.c_health_status==0):
        gameOver()
    if (interaction.twoPlayer == False) and userCar.c_health_status==0:
        gameOver()

def enterPlayerSelect():
    frame.set_mouseclick_handler(clickPlayerSelect)
    frame.set_draw_handler(drawPlayerSelect)

def drawWelcomeScreen(canvas):
    drawAllElements(canvas)
    welcomeScreenGo.draw(canvas)

def enter_game():
    interaction.passBack(bg)
    frame.set_draw_handler(drawGame)
    startTimers()


welcomeScreenGo = Button("https://i.imgur.com/EuhSFX1.jpg", (500, 500), enter_game)


#parameter passed in as canvas
def drawGame(canvas):
    global papaya_time, tree_speed
    # global levelImage
    # image = simplegui.load_image(levelImage)
    # canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (display_width/2,display_height/2), (image.get_width(), image.get_height()))


   #obj_Int.CarsCollison()
    #obj_Int.TouchPapaya()
    #obj_Int.missileCollision()

    drawAllElements(canvas)
    updateAllElements(canvas)

    for i in obstacles:
        if i.pos.x < 0 - i.width/2:
            obstacles.remove(i)
        i.vel = tree1.vel
        i.update()
        i.draw(canvas)
    for bom in bombs:
        bom.update()
        bom.draw(canvas)

    for paps in papaya:
        if paps.pos.x < 0 - paps.width/2:
            papaya.remove(paps)
        paps.vel = tree1.vel
        paps.update()
        paps.draw(canvas)





def timer_handler():
   #print("Papaya Spawn Stuff")
    pass

def spawnObstacle():
    num = random.randint(0, len(OBS)-1)
    obsImg = OBS[num]
    obsRowCol = rowCols[num]
    obs = Obstacle(Vector((DISPLAYW, random.randint(100, 550))), Vector((1, 0)), obsImg, obsRowCol[0], obsRowCol[1])

    obstacles.append(obs)



def spawn_Papaya():
    Papaya_obj = PapayaPick(papayaImg, Vector((random.randrange(300, 950), random.randrange(150, 525))),
                            (papayaImg.get_width()), papayaImg.get_height(), tree1.vel)

    papaya.append(Papaya_obj)


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

def spawnBomb():
    bomb = Bomb(tree1.vel.x)
    bombs.append(bomb)

def drawHelp(canvas):
    helpImage = simplegui.load_image("https://i.imgur.com/yx9xDnx.png")
    canvas.draw_image(helpImage, (helpImage.get_width()/2, helpImage.get_height()/2), (helpImage.get_width(),helpImage.get_height()), (DISPLAYW/2, DISPLAYH/2), (helpImage.get_width(), helpImage.get_height()))
    helpButtonBack.draw(canvas)

def clickHelp(pos):
    if helpButtonBack.contains(pos):
        helpButtonBack.clickBtn()

def enter_help():
    global helpButtonBack
    helpButtonBack = Button("https://i.imgur.com/lOd9C7k.png", (50, 50), enterMainMenu)
    frame.set_mouseclick_handler(clickHelp)
    frame.set_draw_handler(drawHelp)

def level_select(canvas):
    image = simplegui.load_image("https://i.imgur.com/8tYYDrc.png")
    canvas.draw_image(image, (image.get_width()/2, image.get_height()/2), (image.get_width(),image.get_height()), (DISPLAYW/2,DISPLAYH/2), (image.get_width(), image.get_height()))
    level1 = Button("https://i.imgur.com/sZlcBI9.png", (150, 450), enter_level1)
    level2 = Button("https://i.imgur.com/VWL7wfu.png", (500, 450), enter_level2)
    level3 = Button("https://i.imgur.com/wVUdTVL.png", (850, 450), enter_level3)
    backLS = Button("https://i.imgur.com/lOd9C7k.png", (500, 620), enterMainMenu)
    global levelButton
    levelButton = [level1, level2, level3, backLS]
    for x in range(0, len(levelButton)):
        levelButton[x].draw(canvas)

def enter_level_select():
    frame.set_mouseclick_handler(clickLevelSelect)
    frame.set_draw_handler(level_select)

def quit():
    exit(0)

def startTimers():
    timer.start()
    obstacleSpawn.start()
    bombSpawn.start()
    papayaSpawn.start()
    menuMusic.pause()
    menuMusic.rewind()



def stopTimers():
    timer.stop()
    obstacleSpawn.stop()
    bombSpawn.stop()
    papayaSpawn.stop()

def enter_level1():
    bgImage = simplegui.load_image("https://i.imgur.com/erXGov3.png")
    global bg, treeImg, tree1, tree2, interaction
    bg = Background(bgImage, Vector((0, bgImage.get_height()/2)), DISPLAYW)
    treeImg = simplegui.load_image("https://i.imgur.com/ZCBKQ0f.png")
    tree1 = Tree(treeImg, 0 + treeImg.get_height() / 2, DISPLAYW)
    tree2 = Tree(treeImg, DISPLAYH - treeImg.get_height() / 2, DISPLAYW)
    interaction = Interaction(userCar, userCar2, kbd, [tree1, tree2], w1, w2, obstacles, bombs, papaya, twoPlayer)
    interaction.passBack(bg)
    enterWelcomeScreen()



def enter_level2():
    bgImage = simplegui.load_image("https://i.imgur.com/9TUjah2.png")
    global bg, treeImg, tree1, tree2, interaction
    bg = Background(bgImage, Vector((bgImage.get_width()/2, bgImage.get_height()/2)), DISPLAYW)
    treeImg = simplegui.load_image("https://i.imgur.com/OoT9Mzv.png")
    tree1 = Tree(treeImg, 0 + treeImg.get_height() / 2, DISPLAYW)
    tree2 = Tree(treeImg, DISPLAYH - treeImg.get_height() / 2, DISPLAYW)
    interaction = Interaction(userCar, userCar2, kbd, [tree1, tree2], w1, w2, obstacles, bombs, papaya, twoPlayer)
    interaction.passBack(bg)
    enterWelcomeScreen()


def enter_level3():
    bgImage = simplegui.load_image("https://i.imgur.com/AljXcD9.png")
    global bg, treeImg, tree1, tree2, interaction
    bg = Background(bgImage, Vector((bgImage.get_width()/2, bgImage.get_height()/2)), DISPLAYW)
    treeImg = simplegui.load_image("https://i.imgur.com/354gDYv.png")
    tree1 = Tree(treeImg, 0 + treeImg.get_height() / 2, DISPLAYW)
    tree2 = Tree(treeImg, DISPLAYH - treeImg.get_height() / 2, DISPLAYW)
    interaction = Interaction(userCar, userCar2, kbd, [tree1, tree2], w1, w2, obstacles, bombs, papaya, twoPlayer)
    interaction.passBack(bg)
    enterWelcomeScreen()


def enterMainMenu():
    frame.set_mouseclick_handler(clickMainMenu)
    frame.set_draw_handler(draw)
    menuMusic.play()



start = Button("https://i.imgur.com/xoZnCmL.png", (120, 450), enterPlayerSelect)
help = Button("https://i.imgur.com/6OfeKop.png", (470, 450), enter_help)
quit = Button("https://i.imgur.com/zSSFt11.png", (820,450), quit)
arrayButton = [start, help, quit]

onePlayer = Button("https://i.imgur.com/FlJvii8.png", (180, 450), onePlayers)
twoPlayerB = Button("https://i.imgur.com/deyd3aW.png", (800, 450), twoPlayers)
playerButton = [onePlayer, twoPlayerB]
engine = simplegui._load_local_sound("engine.ogg")
retryB = Button("https://i.imgur.com/w8lhgPf.png",(170, 450), enterWelcomeScreen)
mainMenuB = Button("https://i.imgur.com/AK8Yw91.png", (770, 450), enterMainMenu)
gameOverButtons = [retryB, mainMenuB]
menuMusic = simplegui._load_local_sound("music.ogg")
frame = simplegui.create_frame("Papaya Racers", DISPLAYW, DISPLAYH)
frame.set_mouseclick_handler(clickMainMenu)
enterMainMenu()#automatically passes on the canvas
frame.set_keydown_handler(kbd.keyDown)
frame.set_keyup_handler(kbd.keyUp)
timer = simplegui.create_timer(5000, timer_handler)
obstacleSpawn = simplegui.create_timer(4500, spawnObstacle)
bombSpawn = simplegui.create_timer(6000, spawnBomb)
papayaSpawn=simplegui.create_timer(5000,spawn_Papaya)
frame.start()
