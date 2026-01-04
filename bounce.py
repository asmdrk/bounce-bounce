import pygame
import math
# constants/helpers
import random
gravity = 0.981

RADIUS = 2
# gets resultant force magnitude given horizontal and vertical force
def total_force(x,y):
    return math.sqrt(x**2 + y**2)

def get_theta(x,y):
    ratio = x / math.sqrt(x**2 + y**2)
    theta = math.acos(ratio)
    return theta

def bounce(current_pos : pygame.Vector2, screen: pygame.Surface, radius, current_speed: pygame.Vector2):
    # horizontal bounce
    if (current_pos.x + radius) >= screen.get_width() or (current_pos.x - radius) < 0:
        current_speed.x = (-current_speed.x * 0.9) # on a bounce we reduce our speed a littl ebit
    
    # vertical bounce
    if (current_pos.y + radius) >= screen.get_height() or (current_pos.y - radius) < 0:
        current_speed.y = -current_speed.y

def init_speed():
    return pygame.Vector2(random.randint(0,100), random.randint(0,50))

def init_pos():
    return pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1000))
clock = pygame.time.Clock()
running = True
speeds = [pygame.Vector2(random.randint(0,100), random.randint(0,50))]
positions = [pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)]
center = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
font = pygame.font.SysFont('Arial', 30) 
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("purple")
    for current_pos, current_speed in zip(positions, speeds):
        bounce(current_pos, screen, RADIUS, current_speed)
        if current_pos.y > 100:
            current_speed.y += gravity
        # fill the screen with a color to wipe away anything from last frame

        pygame.draw.circle(screen, "red", current_pos, RADIUS)

        current_pos.x += current_speed.x
        current_pos.y += current_speed.y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.MOUSEBUTTONUP]:
        for _ in range(1000):
            positions.append(init_pos())
            speeds.append(init_speed())

    # how many circles?
    text = font.render("Num Circles: " + str(len(positions)), True, (255, 255, 255))  # White text
    screen.blit(text, (screen.get_width() - text.get_width() - 10, 10))  # Position text in the top-right corner

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()