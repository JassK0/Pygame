import pygame
import numpy

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 900, 900
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball")
clock = pygame.time.Clock()
Black = (0,0,0)
Orange = (255,165,0)
Red = (255,0,0)
CIRCLE_CENTER = [WIDTH/2, HEIGHT/2]
CIRCLE_RADIUS = 150
BALL_RADIUS = 10
BALL_POS_1 = [WIDTH/2.2, HEIGHT/2-120]
BALL_POS_2 = [WIDTH/1, HEIGHT/2-11]
gravity = 0.2
ball_velocity = [0,1]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ball_velocity[1] += gravity
    BALL_POS_1[0] += ball_velocity[0]
    BALL_POS_1[1] += ball_velocity[1]
    
    dx = BALL_POS_1[0] - CIRCLE_CENTER[0]
    dy = BALL_POS_1[1] - CIRCLE_CENTER[1]
    dist = (dx*dx + dy*dy)**0.5

    # If ball has hit or passed the boundary
    if dist + BALL_RADIUS >= CIRCLE_RADIUS:
        # 1. normalize the collision normal
        nx = dx / dist
        ny = dy / dist
        # 2. reflect velocity: v' = v - 2*(v·n)*n
        v_dot_n = ball_velocity[0]*nx + ball_velocity[1]*ny
        ball_velocity[0] -= 2 * v_dot_n * nx
        ball_velocity[1] -= 2 * v_dot_n * ny
        # 3. push the ball back onto the boundary so it doesn't get stuck
        BALL_POS_1[0] = CIRCLE_CENTER[0] + nx*(CIRCLE_RADIUS - BALL_RADIUS)
        BALL_POS_1[1] = CIRCLE_CENTER[1] + ny*(CIRCLE_RADIUS - BALL_RADIUS)


    window.fill(Black)
    pygame.draw.circle(window, Orange, CIRCLE_CENTER,CIRCLE_RADIUS,3)
    pygame.draw.circle(window, Red, BALL_POS_1,BALL_RADIUS)
    pygame.draw.circle(window, Red, BALL_POS_2,BALL_RADIUS)
    
    
    
    pygame.display.flip()
    clock.tick(120)
    


pygame.quit()
