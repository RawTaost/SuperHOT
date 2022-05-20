import math

class Player:

    def __init__(self, startX, startY, startAngle, weapon):
        self.x = startX
        self.y = startY
        self.vx = 0
        self.vy = 0
        self.speed = 0.5
        self.angle = startAngle
        self.weapon = weapon
        if self.weapon == None:
            self.image = "textures/Player-Base.png"
        elif self.weapon.type == "pistol":
            self.image = "textures/Player-Pistol.png"
        self.loadedImage = None

    def updateImage(self):
        self.loadedImage = None
        if self.weapon == None:
            self.image = "textures/Player-Base.png"
        elif self.weapon.type == "pistol":
            self.image = "textures/Player-Pistol.png"