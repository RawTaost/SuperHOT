import math

class Draw:

    def __init__(self, pygame, screen, screenWidth, screenHeight):
        self.pygame = pygame
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.backgroundColor = (156, 156, 156)

    def periodic(self, player, projectiles):
        self.drawBackground()
        self.drawPlayer(player)
        self.drawProjectiles(projectiles)

    def drawBackground(self):
        self.screen.fill(self.backgroundColor)

    def drawProjectiles(self, projectiles):
        for p in projectiles:
            img = self.pygame.image.load(p.image).convert_alpha()
            rotImg = self.pygame.transform.rotate(img, (p.angle * 180) / math.pi)
            rect = rotImg.get_rect(center = (p.x, p.y))
            self.screen.blit(rotImg, rect)

    def drawPlayer(self, player):
        img = self.pygame.image.load(player.image).convert_alpha()
        rotImg = self.pygame.transform.rotate(img, (player.angle * 180) / math.pi)
        rect = rotImg.get_rect(center = (player.x, player.y))
        self.screen.blit(rotImg, rect)