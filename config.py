import os
import sys

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
matrix = [[0 for _ in range(size)] for _ in range(size)] # init

# Application
app_name = 'Path Solver'
font_menu = resource_path('fonts/font.otf')
icon = resource_path('images/icon.jpeg')

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