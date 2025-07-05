import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

import config
import menu
import resolution

# -------- Configuration Application --------
pygame.init()
pygame.display.set_caption(config.app_name)
pygame.display.set_icon(pygame.image.load(config.icon))
screen = pygame.display.set_mode((config.size, config.size))
running = True

# -------- Boucle de jeu --------

while running:
    algo_menu = menu.menu(screen)

    #  Cas aucun algorithme
    if len(algo_menu) == 0:
        running = False
    else :
        resolv = resolution.resolution(screen, algo_menu)
        if resolv == 'exit':
            running = False

pygame.quit()