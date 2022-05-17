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
                if Tools.isTouchingCharacter(e.x, e.y, p.x, p.y, e.angle):
                    print("he dead")