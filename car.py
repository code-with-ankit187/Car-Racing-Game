import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings 
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game") 

# Clock
clock = pygame.time.Clock()

# Fonts
font = pygame.font.SysFont("Arial", 30, bold=True)

# Load images
player_img = pygame.image.load("car_player.png")
enemy_img = pygame.image.load("car_enemy.png")

# Resize images
player_img = pygame.transform.scale(player_img, (100, 150))
enemy_img = pygame.transform.scale(enemy_img, (100, 150))


road_color = (50, 50, 50)
line_color = (255, 200, 0)
border_color = (255, 255, 255)

# Player Car
player_w, player_h = 50, 90
player_x = WIDTH // 2 - player_w // 2
player_y = HEIGHT - player_h - 20
player_speed = 6

# Enemy Car
enemy_w, enemy_h = 50, 90
enemy_x = random.randint(120, WIDTH - 120)
enemy_y = -enemy_h
enemy_speed = 5

# Score
score = 0

# Lane Lines
lane_lines = [HEIGHT // 4 * i for i in range(5)]

def draw_road():
    screen.fill(road_color)
    # Road borders
    pygame.draw.rect(screen, border_color, (100, 0, 10, HEIGHT))
    pygame.draw.rect(screen, border_color, (WIDTH - 110, 0, 10, HEIGHT))
    # Lane lines (moving effect)
    for i in range(len(lane_lines)):
        pygame.draw.rect(screen, line_color, (WIDTH//2 - 5, lane_lines[i], 10, 40))
        lane_lines[i] += 10
        if lane_lines[i] > HEIGHT:
            lane_lines[i] = -40

def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_enemy(x, y):
    screen.blit(enemy_img, (x, y))

def show_score():
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

# Main Game Loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 110:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 110 - player_w:
        player_x += player_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_h
        enemy_x = random.randint(120, WIDTH - 120)
        score += 1
        enemy_speed += 0.2  # increase difficulty

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_w, enemy_h)

    if player_rect.colliderect(enemy_rect):
        print("💥 Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    # Draw
    draw_road()
    draw_player(player_x, player_y)
    draw_enemy(enemy_x, enemy_y)
    show_score()

    pygame.display.update()
