import pygame

# ------- Configuration globale ----------

# Matrice
size = 500 # pixels
cell = 15 # pixels
matrix = [[0 for _ in range(size)] for _ in range(size)] # init

# Coordonnées (x, y)
start = (0, 0)
end = (size-1, size-1)

# -------- Algorithme traités -----------

def draw_matrix(screen):
    color = 'gray'
    for i in range(size):
        for j in range(i):
            match((i, j)):
                case 0 :
                    color = '#eb4034'
                    break
                case 1:
                    color = 'lime'
                    break

        pygame.draw.rect(screen, color, (i, j, cell, cell))

# - DFS
# - BFS
# - Dijkstra
# - A* (Blinky)
# - Bidirectional Search
