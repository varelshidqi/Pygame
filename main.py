import pygame
import random
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Permainan Ular di Luar Angkasa")

# Warna
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Ukuran grid
GRID_SIZE = 20

# Ular
snake = [(100, 100), (80, 100), (60, 100)]  # Posisi awal ular (kepala, tubuh, ekor)
snake_dir = (GRID_SIZE, 0)  # Arah gerak ular (ke kanan)

# Makanan
food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
        random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

# Musuh (segitiga)
enemy = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
         random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)

# Bintang latar belakang
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

# Skor
score = 0
font = pygame.font.Font(None, 36)

# Clock untuk mengatur FPS
clock = pygame.time.Clock()
FPS = 8  # Mengatur kecepatan permainan menjadi lebih lambat

# Loop utama
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Gerakan ular dengan tombol panah
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, GRID_SIZE):
        snake_dir = (0, -GRID_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -GRID_SIZE):
        snake_dir = (0, GRID_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (GRID_SIZE, 0):
        snake_dir = (-GRID_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-GRID_SIZE, 0):
        snake_dir = (GRID_SIZE, 0)

    # Update posisi ular
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake = [new_head] + snake[:-1]

    # Periksa jika ular memakan makanan  
    if snake[0] == food:
        snake.append(snake[-1])  # Tambah panjang ular
        food = (random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
        score += 10  # Tambahkan poin

    # Periksa tabrakan dengan musuh
    if snake[0] == enemy:
        running = False

    # Periksa tabrakan dengan dinding
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT):
        running = False

    # Periksa tabrakan dengan tubuh sendiri
    if snake[0] in snake[1:]:
        running = False

    # Update posisi bintang (bergerak perlahan ke bawah)
    stars = [(x, y + 1 if y + 1 < HEIGHT else 0) for x, y in stars]

    # Gambar latar belakang luar angkasa
    screen.fill(BLACK)
    for x, y in stars:
        pygame.draw.circle(screen, WHITE, (x, y), 2)

    # Gambar ular
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Gambar makanan
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Gambar musuh (segitiga)
    pygame.draw.polygon(screen, YELLOW, [(enemy[0], enemy[1]),
                                         (enemy[0] + GRID_SIZE, enemy[1] + GRID_SIZE // 2),
                                         (enemy[0], enemy[1] + GRID_SIZE)])

    # Gambar skor
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update layar
    pygame.display.flip()

    # Atur FPS
    clock.tick(FPS)

# Keluar dari Pygame
pygame.quit()
sys.exit()
