import math
from re import A

class Pistol:

    def __init__(self, x, y, angle, angularVelocity):
        self.x = x
        self.y = y
        self.velocity = 1
        self.angle = angle
        self.anglularVelocity = angularVelocity
        self.image = ""
        self.rotImg = None
        self.rect = None

    def move(self):
        self.x += self.velocity * math.cos(self.angle)
        self.y += self.velocity * math.sin(self.angle)
        self.angle += self.anglularVelocity