import math
import Tools

class Enemy:

    def __init__(self, startX, startY, startAngle, health, weapon):
        self.x = startX
        self.y = startY
        self.vx = 0
        self.vy = 0
        self.speed = 0.3
        self.turnSpeed = 0.025
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
        self.weaponCooldown = 150
        self.cooldown = 0
        self.loadedImg = None
        self.state = "ignorant"
    
    def updateState(self, p):
        if self.state == "ignorant":
            if self.canSeePlayer(p):
                self.state = "alerted"
        elif self.state == "alerted":
            if self.getAngleToPlayer(p) <= 0.2:
                if self.cooldown == 0:
                    self.cooldown = self.weaponCooldown
                    return "attack"
                else: self.cooldown -= 1
            else:
                self.angle += self.turnSpeed * self.getDirectionToPlayer(p)
        return None

    def getPlayerAngle(self, p):
        return math.atan2(p[1] - self.y, p[0] - self.x)

    def getAngleToPlayer(self, p):
        return Tools.getShortestAngle(self.angle, self.getPlayerAngle(p))[0]

    def canSeePlayer(self, p):
        return Tools.getShortestAngle(self.angle, self.getPlayerAngle(p))[0] < math.pi / 4

    def getDirectionToPlayer(self, p):
        return Tools.getShortestAngle(self.angle, self.getPlayerAngle(p))[1]