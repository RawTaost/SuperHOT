import math
import Tools

class Collisions:

    def __init__(self):
        pass

    def periodic(self, player, projectiles, enemies):
        self.projectileEnemy(projectiles, enemies)

    #Collision Detection
    def projectileEnemy(self, projectiles, enemies):
        for e in enemies:
            for p in projectiles:
                if e.rect != None or p.rect != None and p.state == "projectile":
                    if e.rect.colliderect(p.rect):
                        enemies.remove(e)
                        projectiles.remove(p)
                    