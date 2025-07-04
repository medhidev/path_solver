import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import config
import menu

def resolution(screen, algo):
    # -------- Configuration Application --------
    # pygame.display.set_caption('Path Solver')
    # pygame.display.set_icon(pygame.image.load('images/logo.png'))
    # screen = pygame.display.set_mode((config.size, config.size))
    clock = pygame.time.Clock()
    running = True

    # -------- Méthodes --------
    grid_size = config.size // config.cell
    surface = pygame.Surface((config.size, config.size))

    def draw_grid():
        screen.fill('black')
        for i in range(grid_size):
            for j in range(grid_size):
                if config.matrix[i][j] == 0:
                    color = "#4A4A4A"
                elif config.matrix[i][j] == 1:
                    color = "#062839"
                elif config.matrix[i][j] == 2:
                    color = "#1bed53"
                elif config.matrix[i][j] == 3:
                    color = "#edb81b"

                cube = pygame.Rect(i*config.cell, j*config.cell, config.cell, config.cell)
                pygame.draw.rect(surface, color, cube)
                pygame.draw.rect(surface, 'black', cube, 1)

    def set_val(val):
        pos = pygame.mouse.get_pos()
        i = pos[0] // config.cell
        j = pos[1] // config.cell
        config.matrix[i][j] = val

    # -------- Boucle de jeu --------
    held = False
    walls = []
    init_points = []
    depart = False
    arrivee = False
    out = ''

    draw_grid()
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

                    if not depart:
                        set_val(2)
                        init_points.append(pos)
                        depart = True

                    elif depart and not arrivee:
                        set_val(3)
                        init_points.append(pos)
                        arrivee = True

                    draw_grid()

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    held = False

            elif pygame.key.get_pressed()[pygame.K_BACKSPACE]:
                # Suppressions des murs
                for w in walls:
                    i = w[0] // config.cell
                    j = w[1] // config.cell
                    config.matrix[i][j] = 0

                for p in init_points:
                    i = p[0] // config.cell
                    j = p[1] // config.cell
                    config.matrix[i][j] = 0

                # Etat init
                depart = False
                arrivee = False

                draw_grid()

            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                menu.menu(screen)



        if held:
            pos = pygame.mouse.get_pos()
            if pos not in walls:
                walls.append(pos)
                set_val(1)
        
            draw_grid()

        # Mettre à jour l'affichage de l'application
        screen.blit(surface, (0, 0))
        pygame.display.flip()

    return out
