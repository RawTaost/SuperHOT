import math

class Player:

    def __init__(self, startX, startY, startAngle, health, weapon):
        self.x = startX
        self.y = startY
        self.vx = 0
        self.vy = 0
        self.speed = 0.5
        self.angle = startAngle
        self.health = health
        self.weapon = weapon
        if self.weapon.type == "pistol":
            self.image = "textures/Player-Pistol.png"
        else:
            self.image = "textures/Player-Base.png"
        self.loadedImage = None