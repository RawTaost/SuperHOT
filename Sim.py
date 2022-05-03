import math
from sprites.Player import Player
from items.Pistol import Pistol

class Sim:

    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.player = Player(100, 100, math.pi / 2, 1, Pistol(12))

    def getPlayer(self):
        return self.player