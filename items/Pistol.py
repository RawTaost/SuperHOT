import math

class Pistol:

    def __init__(self, ammo):
        self.ammo = ammo
        self.image = None
        self.type = "pistol"
        self.fireType = 'single'

    def hasAmmo(self):
        if self.ammo == 0:
            return False
        else:
            return True

    def fire(self):
        self.ammo -= 1