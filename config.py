# ------- Configuration globale ----------

# Matrice
size = 700 # taille grille pixels
cell = 20 # taille cellule pixels
matrix = [[0 for _ in range(size)] for _ in range(size)] # init

# Alogrithmes
algos = ['DFS', 'BFS', 'Dijkstra', 'A*', 'Bidirectional Search']
font_menu = 'font/font.otf'
menu_x = size * 0.3
menu_y = size * 0.1
space_text = 50 # pixels
font_size = 24

# colors
color_btn = '#7b9cc8'
color_btn_selected = "#fde71d"
background_menu = '#252551'
color_text = [color_btn for _ in range(len(algos))]