import math

class Bullet:

    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.velocity = 5
        self.image = "textures/Bullet.png"

    def move(self):
        self.x += self.velocity * math.cos(self.angle)
        self.y += self.velocity * math.sin(self.angle)