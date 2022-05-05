import math
import pygame
from sprites.Player import Player
from items.Pistol import Pistol

class Sim:

    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.cursorX = pygame.mouse.get_pos()[0]
        self.cursorY = pygame.mouse.get_pos()[1]
        self.player = Player(100, 100, math.pi / 2, 1, Pistol(12))

    def movePlayer(self):
        #Get Direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.vy = -self.player.speed
        elif keys[pygame.K_s]:
            self.player.vy = self.player.speed
        else:
            self.player.vy = 0

        if keys[pygame.K_d]:
            self.player.vx = self.player.speed
        elif keys[pygame.K_a]:
            self.player.vx = -self.player.speed
        else:
            self.player.vx = 0

        #Get Angle
        self.cursorX = pygame.mouse.get_pos()[0]
        self.cursorY = pygame.mouse.get_pos()[1]

        self.player.angle = -math.atan2(self.cursorY - self.player.y, self.cursorX - self.player.x) - math.pi / 2

        #Move
        self.player.x += self.player.vx
        self.player.y += self.player.vy

    def update(self):
        self.movePlayer()

    def getPlayer(self):
        return self.player