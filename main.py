import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import config
import menu
import resolution

# -------- Configuration Application --------
pygame.init()
pygame.display.set_caption('Path Solver')
pygame.display.set_icon(pygame.image.load('images/logo.png'))
screen = pygame.display.set_mode((config.size, config.size))
running = True
# clock = pygame.time.Clock()

# -------- Boucle de jeu --------

while running:
    algo_menu = menu.menu(screen)

    #  SI il y a pas d'algo choisi
    if len(algo_menu) == 0:
        running = False
    else :
        resolv = resolution.resolution(screen, algo_menu)
        if resolv == 'exit':
            running = False

pygame.quit()