import math

class Draw:

    def __init__(self, pygame, screen, screenWidth, screenHeight):
        self.pygame = pygame
        self.screen = screen
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.backgroundColor = (156, 156, 156)
        self.font = self.pygame.font.SysFont("consolas", 50)
        # print(self.pygame.font.get_fonts())

    def periodic(self, player, projectiles, enemies):
        self.drawBackground()
        self.drawProjectiles(projectiles)
        self.drawPlayer(player)
        self.drawEnemies(enemies)
        self.drawInfoPanel(player, enemies)

    def drawBackground(self):
        self.screen.fill(self.backgroundColor)

    def drawInfoPanel(self, player, enemies):
        self.pygame.draw.rect(self.screen, (100, 100, 100), (0, 0, 340, 130))
        if player.weapon == None:
            ammoInfo = self.font.render("No Weapon", True, (31, 255, 65))
        else:
            if player.weapon.ammo == 0:
                ammoInfo = self.font.render("No Ammo!", True, (31, 255, 65))
            else:
                ammoInfo = self.font.render(f"Ammo: {player.weapon.ammo}", True, (31, 255, 65))
        self.screen.blit(ammoInfo, (10, 10))
        enemyInfo = self.font.render(f"{len(enemies)} Enemie(s)", True, (31, 255, 65))
        self.screen.blit(enemyInfo, (10, 70))

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