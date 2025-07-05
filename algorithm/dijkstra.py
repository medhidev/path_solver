import config
import pygame
import time

def dijkstra(surface):
    # Scan de l'ensemble des noeuds

    for i in range(config.grid_size):
        for j in range(config.grid_size):
            config.matrix[j][i] = 4
            
            # Met à jour l'affichage
            config.draw_grid(surface)
            config.screen.blit(surface, (0, 0))
            pygame.display.update()      
            time.sleep(0.02) 

            
