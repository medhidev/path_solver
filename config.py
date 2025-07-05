import os
import sys
import pygame

# -------- Méthodes --------

# Gestions des fichiers externes (StackOverflow)
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# ------- Configuration globale ----------

# Matrice
size = 700 # taille grille pixels
cell = 20 # taille cellule pixels
matrix = [[0 for _ in range(size)] for _ in range(size)] # initialisation de la matrice
grid_size = size // cell
start = ()
end = ()

# Application
app_name = 'Path Solver'
font_menu = resource_path('fonts/font.otf')
icon = resource_path('images/icon.jpeg')
screen = screen = pygame.display.set_mode((size, size))

# Alogrithmes
algos = ['DFS', 'BFS', 'Dijkstra', 'A*', 'Bidirectional Search']
menu_x = size * 0.3
menu_y = size * 0.1
space_text = 50 # pixels
font_size = 24

# Couleurs
color_btn = '#7b9cc8'
color_btn_selected = "#fde71d"
background_menu = '#252551'
color_text = [color_btn for _ in range(len(algos))]

# ---------- Méthodes ----------

def set_val(pos, val):
    i = pos[0] // cell
    j = pos[1] // cell
    matrix[i][j] = val

def draw_grid(surface):
    for i in range(grid_size):
        for j in range(grid_size):
            if matrix[i][j] == 0:
                color = "#4A4A4A"
            elif matrix[i][j] == 1:
                color = "#062839"
            elif matrix[i][j] == 2:
                color = "#1bed53"
            elif matrix[i][j] == 3:
                color = "#edb81b"

            # Différents algorithmes
            elif matrix[i][j] == 4:  # Dijkstra
                color = "#ff3939"

            cube = pygame.Rect(i*cell, j*cell, cell, cell)
            pygame.draw.rect(surface, color, cube)
            pygame.draw.rect(surface, 'black', cube, 1)