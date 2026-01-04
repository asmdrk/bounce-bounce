import pygame
import math
# constants/helpers
import random
gravity = 0.981

# gets resultant force magnitude given horizontal and vertical force
def total_force(x,y):
    return math.sqrt(x**2 + y**2)

def get_theta(x,y):
    ratio = x / math.sqrt(x**2 + y**2)
    theta = math.acos(ratio)
    return theta

def bounce(current_pos : pygame.Vector2, screen: pygame.Surface, radius, dx, dy):
    # horizontal bounce
    if (current_pos.x + radius) >= screen.get_width() or (current_pos.x - radius) < 0:
        dx = (-dx * 0.9)
    if (current_pos.y + radius) >= screen.get_height() or (current_pos.y - radius) < 0:
        dy = -dy
    
    return (dx,dy)
    # vertical bounce

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1000))
clock = pygame.time.Clock()
running = True
dx = random.randint(0,100)
dy = random.randint(0,50)
current_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dx,dy = bounce(current_pos, screen, 40, dx, dy)
    if current_pos.y > 100:
        dy += gravity
    print("oof dy:", dy)
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", current_pos, 40)

    current_pos.x += dx
    current_pos.y += dy

    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()