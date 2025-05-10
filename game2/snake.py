import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 199, 100)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake and point setup
snake = [pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE), pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE), pygame.Rect(100, 100, CELL_SIZE, CELL_SIZE)]
direction = pygame.K_RIGHT
points = [
    pygame.Rect(random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                        random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE),
    pygame.Rect(random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                        random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE)
]

bombs = [
        pygame.Rect(random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                        random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE,
                        CELL_SIZE, CELL_SIZE)
]
eaten_amount = 0
score = 0
eaten_sound = pygame.mixer.Sound("game2/coin.wav")
bomb_sound = pygame.mixer.Sound("game2/bomb.mp3")
die_sound = pygame.mixer.Sound("game2/die.mp3")

bomb_image = pygame.image.load("game2/bomb.png").convert_alpha()
bomb_image = pygame.transform.scale(bomb_image, (CELL_SIZE, CELL_SIZE))



clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)



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

# Game loop
while True:
    screen.fill(WHITE)

    # Handle quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle input
    keys = pygame.key.get_pressed()
    for key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
        if keys[key]:  
            direction = key
    def game_over():
        die_sound.play()
        game_over_text = font.render("Game Over!", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    # Move snake
    new_head = move_snake()

    # Check collision with walls or self
    if (new_head.left < 0 or new_head.right > WIDTH or
        new_head.top < 0 or new_head.bottom > HEIGHT or
        new_head.collidelist(snake) != -1): # self collide check (-1 is checking the things
        #behind the head of the list (not possibele to collide with the one right behinf it)) 
        game_over()


    snake.insert(0, new_head)

    eaten = False
    
    for p in points:

        if new_head.colliderect(p):
            p.x = random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE
            p.y = random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE
            eaten_sound.play()
            score += 1
            eaten_amount += 1
            eaten = True
            
            if eaten_amount % 3 == 0:
                new_bomb = pygame.Rect(
                    random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                    random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE,
                    CELL_SIZE, CELL_SIZE)
                bombs.append(new_bomb)
            break
        

    if not eaten:
        snake.pop()
    for b in bombs:
        if new_head.colliderect(b):
            bomb_sound.play()
            game_over()


    # Draw snake and point
    score_text = font.render(f"Score {score}",True,BLACK)
    screen.blit(score_text,(0,0))
    for segment in snake:
        pygame.draw.rect(screen, GREEN, segment)
    for p in points:
        pygame.draw.rect(screen,RED,p)
    for b in bombs:
        screen.blit(bomb_image,b)


    pygame.display.update()
    clock.tick(10)
