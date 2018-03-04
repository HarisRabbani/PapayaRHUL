from user301_dZJL5znAdk_0 import Vector
from user301_P0g9WpMgCh_0 import Line
from user301_FM91pKbpyD_3 import Keyboard

class RegularPolygon:
    def __init__(self, sides, pos, size, Keyboard, CANVAS_HEIGHT, CANVAS_WIDTH):
        self.CANVAS_HEIGHT = CANVAS_HEIGHT
        self.CANVAS_WIDTH = CANVAS_WIDTH
        self.Keyboard = Keyboard
        self.sides = sides
        self.pos = pos
        self.vel = Vector()
        self.size = size
        self.generator = Vector(0, -self.size)
        self.vertices = []
        self.botVert = self.generator+self.pos
       
        
    def computeVertices(self):
        angle = 360 / self.sides
        gen = self.generator.copy()
        self.vertices = []
        for i in range(self.sides):
            self.vertices.append(self.pos + gen)
            gen.rotate(angle)

    def computeSides(self):
        self.computeVertices()
        self.lines = [ Line(self.vertices[i], self.vertices[(i + 1) % len(self.vertices)])
                       for i in range(len(self.vertices)) ]
    def draw(self, canvas):
        self.computeSides()
        for line in self.lines:
            line.draw(canvas)

    def drawGenerator(self, canvas):
        line = Line(self.pos, self.pos + self.generator)
        line.draw(canvas)
       
    def bottomVert(self):#bottom corner position
        return self.vertices[(self.sides + 1) % len(self.vertices)]
    def bottomVertVec(self):
        return Vector((self.bottomVert().x),(self.bottomVert().y))
      
    def topVert(self): #top corner position
        return (self.generator+self.pos)
    def topVertVec(self):
        return Vector((self.topVert().x),(self.topVert().y))
    def forVec(self):
        return Vector((self.topVertVec().x-self.bottomVertVec().x),(self.topVertVec().y-self.bottomVertVec().y))
        
    
    def forwardVel(self):
        return Vector(self.topVert-self.bottomVert) #self.topVert.x #-self.bottomVert.x #)/10),((self.topVert.y-self.bottomVert.y)/10))
    
    def print2(self):
        return Vector((self.vertices[(self.sides + 1) % len(self.vertices)])-(self.generator+self.pos))
    
    def update(self):
        self.pos.add(self.vel)
        self.vel.multiply(0.85)
        
        if self.pos.y>self.CANVAS_HEIGHT:
            self.pos.y = 0
        if self.pos.y<0:
            self.pos.y = self.CANVAS_HEIGHT
        if self.pos.x>self.CANVAS_WIDTH:
            self.pos.x = 0
        if self.pos.x<0:
            self.pos.x = self.CANVAS_WIDTH


        if self.Keyboard.right and self.Keyboard.left: 
                self.vel.add(Vector(0, 0))
        if self.Keyboard.right and self.Keyboard.up: 
                self.vel.add(Vector(1,-1.5 ))
        if self.Keyboard.left and self.Keyboard.up: 
                self.vel.add(Vector(-1,-1.5))

        if self.Keyboard.right and self.Keyboard.down: 
                self.vel.add(Vector(1,1.5))
        if self.Keyboard.left and self.Keyboard.down: 
                self.vel.add(Vector(-1,1.5))    

        if self.Keyboard.up: 
                self.vel.add(Vector(self.forVec().x/100,self.forVec().y/100))
        if self.Keyboard.down: 
                self.vel.add(Vector(-self.forVec().x/100,-(self.forVec().y)/100))
        if self.Keyboard.right:
                self.generator.rotate(1.5)
        if self.Keyboard.left:
                self.generator.rotate(-1.5)
       
