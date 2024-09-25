import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Tentukan ukuran layar
screen = pygame.display.set_mode((640, 480))

# Tentukan warna (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Isi layar dengan warna hitam
    screen.fill(BLACK)

    # Update tampilan
    pygame.display.flip()

pygame.quit()
sys.exit()
