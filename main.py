from config import *
from Background import *

pygame.init()

# Create a window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set game icon
icon = pygame.image.load(ICON_PATH).convert()
pygame.display.set_icon(icon)
pygame.display.set_caption(GAME_NAME)

# set pygame clock
clock = pygame.time.Clock()

# set game background
background = Background(GAME_BG_PATH, GAME_BG_SPEED, window)

# set the running loop
running = True
while running:
    clock.tick(FRAMES_PER_SEC)
    background.display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()


