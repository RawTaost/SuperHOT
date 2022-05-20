import math
import pygame
from sprites.Player import Player
from sprites.Bullet import Bullet
from items.Pistol import Pistol
from sprites.Enemy import Enemy
from sprites.Pistol import Pistol as PistolObject

class Sim:

    def __init__(self, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.cursorX = pygame.mouse.get_pos()[0]
        self.cursorY = pygame.mouse.get_pos()[1]
        self.player = Player(100, 100, math.pi / 2, Pistol(12))
        self.projectiles = []
        self.enemies = []

    def init(self):
        self.enemies.append(Enemy(500, 500, math.pi / 2, Pistol(12)))
        self.enemies.append(Enemy(1000, 200, math.pi, Pistol(12)))

    def update(self):
        self.movePlayer()
        self.moveEnemies()
        self.moveProjectiles()

    def shoot(self, character):
        character.weapon.fire()
        direction = -character.angle - math.pi / 2
        r = 68
        self.projectiles.append(Bullet(character.x + r * math.cos(character.angle), character.y + r * math.sin(character.angle), character.angle))

    def throwWeapon(self, character):
        r = 68
        if character.weapon.type == "pistol":
            self.projectiles.append(PistolObject(character.x + r * math.cos(character.angle), character.y + r * math.sin(character.angle), character.angle, 0.05))
        character.weapon = None
        character.updateImage()

    def attack(self, character):
        if character.weapon == None:
            pass
        else:
            if character.weapon.hasAmmo():
                self.shoot(character)
            else:
                self.throwWeapon(character)

    def moveProjectiles(self):
        for p in self.projectiles:
            if p.x < 0 or p.x > self.screenWidth or p.y < 0 or p.y > self.screenHeight:
                self.projectiles.remove(p)
            else:
                p.move()

    def moveEnemies(self):
        for e in self.enemies:
            e.x += e.vx
            e.y += e.vy
            if e.updateState((self.player.x, self.player.y)) == "attack":
                self.attack(e)

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

        self.player.angle = math.atan2(self.cursorY - self.player.y, self.cursorX - self.player.x)

        #Move
        self.player.x += self.player.vx
        self.player.y += self.player.vy

    def getPlayer(self):
        return self.player

    def getProjectiles(self):
        return self.projectiles

    def getEnemies(self):
        return self.enemies
        