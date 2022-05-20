import math

class Pistol:

    def __init__(self, x, y, angle, angularVelocity):
        self.x = x
        self.y = y
        self.velocity = 1
        self.decayRate = 0.9989
        self.moveAngle = angle
        self.angle = angle
        self.anglularVelocity = angularVelocity
        self.image = "textures/Pistol.png"
        self.loadedImage = None
        self.rotImg = None
        self.rect = None
        self.state = "projectile"

    def move(self):
        self.x += self.velocity * math.cos(self.moveAngle)
        self.y += self.velocity * math.sin(self.moveAngle)
        self.angle += self.anglularVelocity
        self.velocity *= self.decayRate

        if self.velocity < 0.3:
            self.anglularVelocity = 0
            self.velocity = 0
            self.state = "item"

