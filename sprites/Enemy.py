import math
from sys import get_asyncgen_hooks
from webbrowser import get

class Enemy:

    def __init__(self, startX, startY, startAngle, health, weapon):
        self.x = startX
        self.y = startY
        self.vx = 0
        self.vy = 0
        self.speed = 0.3
        self.angle = startAngle
        self.health = health
        self.weapon = weapon
        self.rotImg = None
        self.rect = None
        self.width = 64
        self.height = 38
        if self.weapon.type == "pistol":
            self.image = "textures/Enemy-Pistol.png"
        else:
            self.image = "textures/Enemy-Base.png"
        self.loadedImg = None
        self.state = "patroling"
    
    def updateState(self, p):
        if self.state == "alerted":
            if abs(self.getAngleToPlayer(p) - self.angle) < 0.2:
                return "attack"
            else:
                self.angle += 0.05
        elif self.state == "patroling":
            self.angle += 0.01
            if abs(self.getAngleToPlayer(p) - self.angle) < 0.785:
                self.state = "alerted"
        return None

    def getAngleToPlayer(self, p):
        return math.atan2(p[1] - self.y, p[0] - self.x)