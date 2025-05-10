import pygame
import sys
import random

 # Initialize Pygame
pygame.init()

 # Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame Window!")

    # Create a player rectangle
player = pygame.Rect(300, 200, 50, 50)
point = pygame.Rect(100, 50, 50, 50)
player_speed = 1
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,199,100)
score = 0
font = pygame.font.SysFont(None, 36)

coin_sound = pygame.mixer.Sound("game1/coin.wav")



 # Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed    
        
    # Keep the player inside the screen
    if player.left < 0:
        player.left = 0
    if player.right > 800:
        player.right = 800
    if player.top < 0:
        player.top = 0
    if player.bottom > 600:
        player.bottom = 600     
        
    
    #if player touches point
    if player.colliderect(point):
        score += 1
        coin_sound.play()
        #move point to random spot
        point.x = random.randint(0, 750)
        point.y = random.randint(0, 550)

    
    if score >= 5:
        screen.fill(GREEN)
        win_text = font.render("YOU WIN!!", True, WHITE)
        screen.blit(win_text,(300,300))
    else:

        # Draw everything
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, player)
        pygame.draw.rect(screen, GREEN, point)
        score_text = font.render(f"Score {score}", True, (0,0,0))
        screen.blit(score_text,(0,0))

    pygame.display.update()