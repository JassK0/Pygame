import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 100)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Game setup
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Snake and direction
snake = [pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE)]
direction = pygame.K_RIGHT

# Food
food = pygame.Rect(
    random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
    random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE,
    CELL_SIZE, CELL_SIZE
)

# Score
score = 0

def move_snake():
    head = snake[0].copy()
    if direction == pygame.K_LEFT:
        head.x -= CELL_SIZE
    elif direction == pygame.K_RIGHT:
        head.x += CELL_SIZE
    elif direction == pygame.K_UP:
        head.y -= CELL_SIZE
    elif direction == pygame.K_DOWN:
        head.y += CELL_SIZE
    return head

def game_over():
    text = font.render("Game Over!", True, RED)
    screen.blit(text, (WIDTH // 2 - 80, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Main game loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != pygame.K_RIGHT:
        direction = pygame.K_LEFT
    elif keys[pygame.K_RIGHT] and direction != pygame.K_LEFT:
        direction = pygame.K_RIGHT
    elif keys[pygame.K_UP] and direction != pygame.K_DOWN:
        direction = pygame.K_UP
    elif keys[pygame.K_DOWN] and direction != pygame.K_UP:
        direction = pygame.K_DOWN

    # Move snake
    new_head = move_snake()

    # Check collisions
    if (new_head.left < 0 or new_head.right > WIDTH or
        new_head.top < 0 or new_head.bottom > HEIGHT or
        new_head.collidelist(snake) != -1):# Check for self-collision: collidelist returns -1 if no collision.
        # If it returns any index (i.e., not -1), the snake collided with itself and the game ends
        game_over()

    snake.insert(0, new_head)

    if new_head.colliderect(food):
        score += 1
        food.x = random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE
        food.y = random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE
    else:
        snake.pop()

    # Draw everything
    for segment in snake:
        pygame.draw.rect(screen, GREEN, segment)

    pygame.draw.rect(screen, RED, food)
    
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(10)
