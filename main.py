# Désactiver le message en console
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Example file showing a circle moving on screen
import pygame
import config
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((config.size, config.size))
clock = pygame.time.Clock()
running = True

center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

for _ in range (20):
    print([])
    config.matrix[random.randint(0, config.size-1)][random.randint(0, config.size-1)] = 1

while running:
    clock.tick(60)

    # Events Listener
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#404040")

    # config.draw_matrix(screen)
    color = 'gray'
    for i in range(config.size):
        for j in range(config.size):
            if (config.matrix[i][j] == 0):
                color = '#eb4034'
            elif (config.matrix[i][j] == 1):
                color = '#1da859'
            pygame.draw.rect(screen, color, (i, j, config.cell, config.cell))

    # pygame.draw.circle(screen, "red", player_pos, 40)
    


    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt



    # Display
    pygame.display.flip()

# def color_matrix():
#     for i in range(config.size):
#         for j in range(i):
#             match((i, j)):
#                 # Départ - Mur - Arrivée
#                 case 0 :
#                     pygame.draw.rect(screen, '#eb4034' , (50, 50, 100, 100))
#                     break
#                 case 1:
#                     print('mur')
#                     break
#                 case -1:
#                     print('fin')
#                     break

#             # Couleurs cases Algorithme

pygame.quit()