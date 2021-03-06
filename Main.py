import pygame
import math
from Draw import Draw
from Sim import Sim
from Collisions import Collisions

pygame.init()
m_screenWidth = 1440
m_screenHeight = 845
m_screen = pygame.display.set_mode([m_screenWidth, m_screenHeight])
pygame.display.set_caption("SuperHOT")

m_draw = Draw(pygame, m_screen, m_screenWidth, m_screenHeight)
m_sim = Sim(m_screenWidth, m_screenHeight)
m_sim.init()
m_collisions = Collisions()

m_running = True
while m_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            m_running = False
        if event.type == pygame.MOUSEBUTTONUP:
            m_sim.attack(m_sim.getPlayer())
    ##########
    m_sim.update()
    m_draw.periodic(m_sim.getPlayer(), m_sim.getProjectiles(), m_sim.getEnemies())
    m_collisions.periodic(m_sim.getPlayer(), m_sim.getProjectiles(), m_sim.getEnemies())
    ##########
    pygame.display.flip()
pygame.quit()