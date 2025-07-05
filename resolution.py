import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import config
import menu

# Algorithmes
from algorithm.dijkstra import *
from algorithm.a_star import *
from algorithm.dfs import *
from algorithm.bfs import *
from algorithm.bidirsearch import *

def resolution(screen, algo:str):
    # -------- Configuration Application --------

    clock = pygame.time.Clock()
    running = True

    # -------- Méthodes --------
    surface = pygame.Surface((config.size, config.size))

    # -------- Boucle de jeu --------
    held = False
    walls = []
    init_points = []
    out = ''

    config.draw_grid(surface)
    while running:
        clock.tick(60)
        screen.fill('black')

        # ------ Ecouteurs d'Events ------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                out = 'exit'
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    held = True
                elif event.button == 3:
                    pos = pygame.mouse.get_pos()

                    if len(config.start) == 0:
                        config.set_val(pos, 2)
                        config.start = pos
                        init_points.append(config.start)

                    elif len(config.start) != 0 and len(config.end) == 0:
                        config.set_val(pos, 3)
                        config.end = pos
                        init_points.append(config.end)

                    config.draw_grid(surface)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    held = False

            elif pygame.key.get_pressed()[pygame.K_BACKSPACE]:

                # Reset complet de la matrice
                for i in range(config.grid_size):
                    for j in range(config.grid_size):
                        if config.matrix[i][j] != 0:
                            config.matrix[i][j] = 0

                # Mise à jour de l'affichage
                config.draw_grid(surface)

            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                menu.menu(screen)

            elif pygame.key.get_pressed()[pygame.K_RETURN]:
                print(algo.lower())
                if algo.lower() == 'dijkstra':
                    dijkstra(surface)

                
                        


        if held:
            pos = pygame.mouse.get_pos()
            if pos not in walls:
                walls.append(pos)
                config.set_val(pos, 1)
        
            config.draw_grid(surface)

        # Mettre à jour l'affichage de l'application
        screen.blit(surface, (0, 0))
        pygame.display.flip()

    return out
