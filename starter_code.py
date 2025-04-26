import pygame
import sys

 # Initialize Pygame
pygame.init()

 # Set up the screen
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My First Pygame Window!")

 # Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()