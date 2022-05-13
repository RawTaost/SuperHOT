import math

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