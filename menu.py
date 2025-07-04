import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
import config

def menu(screen):

    clock = pygame.time.Clock()
    running = True
    out = ''

    # -------- Méthodes --------

    menu = pygame.Surface((config.size, config.size))
    count_letters = []
    vect_texts = []
    char_width = round(config.font_size * 0.62) # 62% pour la largeur par rapport à la hauteur
    font = pygame.font.Font(config.font_menu, config.font_size)
        
    def display_menu():
        menu.fill(config.background_menu)
        x = config.menu_x
        y = config.menu_y

        # Vide les anciennes valeurs
        count_letters.clear()
        vect_texts.clear()

        for i in range(len(config.algos)):
            count_letters.append(len(config.algos[i])) # nombre de caractères
            y += config.space_text # espacement
            text = font.render(config.algos[i], True, config.color_text[i])
            menu.blit(text, (x, y))

            vect_texts.append([(x, y), (x+char_width*count_letters[i], y + config.font_size)])


    # -------- Boucle de jeu --------

    display_menu()
    while running:
        clock.tick(60)
        pos = pygame.mouse.get_pos()

        # ------ Ecouteurs d'Events ------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(config.algos)):
                    # Se situe dans les bonnes coordonnées
                    if (vect_texts[i][0][0] <= pos[0] <= vect_texts[i][1][0]) and (vect_texts[i][0][1] <= pos[1] <= vect_texts[i][1][1]):
                        out = config.algos[i]
                        running = False

            elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

        for i in range(len(config.algos)):
            # Se situe dans les bonnes coordonnées
            if (vect_texts[i][0][0] <= pos[0] <= vect_texts[i][1][0]) and (vect_texts[i][0][1] <= pos[1] <= vect_texts[i][1][1]):
                config.color_text[i] = config.color_btn_selected
                
            else:
                config.color_text[i] = config.color_btn

        # Mise à jour graphique
        display_menu()
        screen.blit(menu, (0, 0))
        pygame.display.flip()


    return out