import pygame
import random
import sys

# Inisialisasi Pygame
pygame.init()

# Tentukan ukuran layar
screen = pygame.display.set_mode((640, 480))

# Atur judul window
pygame.display.set_caption("Random Color Button")

# Tentukan warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tentukan ukuran dan posisi tombol
button_color = (0, 200, 0)
button_rect = pygame.Rect(270, 200, 100, 50)

# Fungsi untuk menghasilkan warna acak
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Main loop
running = True
bg_color = WHITE  # Warna latar awal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Jika tombol ditekan
            if button_rect.collidepoint(event.pos):
                bg_color = random_color()  # Ubah warna latar

    # Isi layar dengan warna latar belakang
    screen.fill(bg_color)

    # Gambar tombol
    pygame.draw.rect(screen, button_color, button_rect)

    # Tambahkan teks pada tombol
    font = pygame.font.Font(None, 36)
    text = font.render("Change", True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    # Update tampilan
    pygame.display.flip()

# Tutup Pygame dengan benar
pygame.quit()
sys.exit()
