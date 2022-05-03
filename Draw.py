import math

class Draw:

    def __init__(self, pygame, screen, screenWidth, screenHeight):
        self.pygame = pygame
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.backgroundColor = (156, 156, 156)

    def periodic(self, player):
        self.drawBackground()
        self.drawPlayer(player)

    def drawBackground(self):
        self.screen.fill(self.backgroundColor)

    def drawPlayer(self, player):
        img = self.pygame.image.load(player.image).convert_alpha()
        rect = img.get_rect(center = [player.x, player.y])
        self.screen.blit(img, rect)