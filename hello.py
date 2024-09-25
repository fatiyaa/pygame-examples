import pygame
import sys

# Inisialisasi Pygame
pygame.init()

# Tentukan ukuran layar
screen = pygame.display.set_mode((640, 480))

# Tentukan warna (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Atur judul window
pygame.display.set_caption("Hello Pygame")

# Pilih font dan ukuran
font = pygame.font.Font(None, 74)

# Render teks
text = font.render("Hello Pygame", True, WHITE)

# Posisi teks di tengah layar
text_rect = text.get_rect(center=(320,240))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Isi layar dengan warna hitam
    screen.fill(BLACK)

    # Gambar teks di layar
    screen.blit(text, text_rect)

    # Update tampilan
    pygame.display.flip()

pygame.quit()
sys.exit()
