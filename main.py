import pygame
from config import *

pygame.init()

# Create a window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set game icon
icon = pygame.image.load(ICON_PATH).convert()
pygame.display.set_icon(icon)
pygame.display.set_caption(GAME_NAME)

# set pygame clock
clock = pygame.time.Clock()

# set the running loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(FRAMES_PER_SEC)


