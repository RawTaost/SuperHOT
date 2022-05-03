import math

class Player:

    def __init__(self, startX, startY, startAngle, health, weapon):
        self.x = startX
        self.y = startY
        self.angle = startAngle
        self.health = health
        self.weapon = weapon
        if self.weapon.type == "pistol":
            self.image = "textures/Player-Pistol.png"
        else:
            self.image = "textures/Player-Base.png"