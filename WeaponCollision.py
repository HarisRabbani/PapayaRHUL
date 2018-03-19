from Vector import Vector
import math


class WeaponCollision: # Old code - This could be used.
    def __init__(self):
        self.weapons = []
        self.walls = []
        self.inCollision = False

    def addWall(self, wall):
        self.walls.append(wall)

    def addWeapon(self, weapon):
        self.weapons.append(weapon)

    def update(self):
        for wall in self.walls:
            for weapon in self.weapons:
                if wall.hit(weapon):
                    weapon.bounce(wall.normal)
                    if weapon.hitCount == 0:
                        weapon.hitCount += 1
                    else:
                        weapon.explosion = True
                weapon.update()

    def draw(self, canvas):
        self.update()
        for weapon in self.weapons:
            weapon.draw(canvas)
        for wall in self.walls:
            wall.draw(canvas)

