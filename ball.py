import pygame
import random
import sys
from time import sleep

# Inisialisasi Pygame
pygame.init()

# Tentukan ukuran layar
screen = pygame.display.set_mode((640, 480))

# Atur judul window
pygame.display.set_caption("Random Color Button with Moving Ball")

# Tentukan warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Tentukan ukuran dan posisi tombol
button_color = (0, 200, 0)
button_rect = pygame.Rect(270, 200, 100, 50)

# Fungsi untuk menghasilkan warna acak
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Variabel untuk bola
ball_color = (255, 0, 0)
ball_radius = 20
ball_x = random.randint(ball_radius, 640 - ball_radius)
ball_y = random.randint(ball_radius, 480 - ball_radius)
ball_dx = random.choice([-1, 1])
ball_dy = random.choice([-1, 1])

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
                ball_color = random_color()  # Ubah warna bola

    # Isi layar dengan warna latar belakang
    screen.fill(bg_color)
    # Gerakkan bola
    ball_x += ball_dx
    ball_y += ball_dy
    sleep(0.001)
    # Pantulkan bola jika mencapai tepi layar
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= 640:
        ball_dx *= -1
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= 480:
        ball_dy *= -1

    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Gambar tombol
    pygame.draw.rect(screen, button_color, button_rect)

    # Tambahkan teks pada tombol
    font = pygame.font.Font(None, 36)
    text = font.render("Change", True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    # Gambar bola yang bergerak

    # Update tampilan
    pygame.display.flip()

# Tutup Pygame dengan benar
pygame.quit()
sys.exit()
