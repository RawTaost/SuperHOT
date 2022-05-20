import math

class Draw:

    def __init__(self, pygame, screen, screenWidth, screenHeight):
        self.pygame = pygame
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.backgroundColor = (156, 156, 156)

    def periodic(self, player, projectiles, enemies):
        self.drawBackground()
        self.drawProjectiles(projectiles)
        self.drawPlayer(player)
        self.drawEnemies(enemies)

    def drawBackground(self):
        self.screen.fill(self.backgroundColor)

    def drawEnemies(self, enemies):
        for e in enemies:
            if e.loadedImage == None:
                e.loadedImage = self.pygame.image.load(e.image).convert_alpha()
            e.rotImg = self.pygame.transform.rotate(e.loadedImage, ((-e.angle - math.pi / 2) * 180) / math.pi)
            e.rect = e.rotImg.get_rect(center = (e.x, e.y))
            self.screen.blit(e.rotImg, e.rect)


    def drawProjectiles(self, projectiles):
        for p in projectiles:
            if p.rotImg == None:
                p.loadedImage = self.pygame.image.load(p.image).convert_alpha()
            p.rotImg = self.pygame.transform.rotate(p.loadedImage, ((-p.angle - math.pi / 2) * 180) / math.pi)
            p.rect = p.rotImg.get_rect(center = (p.x, p.y))
            self.screen.blit(p.rotImg, p.rect)

    def drawPlayer(self, player):
        if player.loadedImage == None:
            player.loadedImage = self.pygame.image.load(player.image).convert_alpha()
        rotImg = self.pygame.transform.rotate(player.loadedImage, ((-player.angle - math.pi / 2) * 180) / math.pi)
        rect = rotImg.get_rect(center = (player.x, player.y))
        self.screen.blit(rotImg, rect)