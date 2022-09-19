from config import *
from Background import *
from ShootingSystem import *

pygame.init()

# Create a window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# set game icon
icon = pygame.image.load(ICON_PATH).convert()
pygame.display.set_icon(icon)
pygame.display.set_caption(GAME_NAME)

# set pygame clock
clock = pygame.time.Clock()

# set player
player = Player(PLAYER_IMG_PATH, PLAYER_SPEED)

# set game background
background = Background(GAME_BG_PATH, GAME_BG_SPEED, window)

# set a cartridge for player
bullets = [Bullet(PLAYER_BULLET_IMG_PATH, PLAYER_BULLET_SPEED) for _ in range(BULLET_CARTRIDGE)]

# set player's shooting system
player_shoot = Shooting(bullets, PLAYER_BULLET_INTERVAL, player, window)

# set the running loop
running = True
while running:
    clock.tick(FRAMES_PER_SEC)
    pressed_key = pygame.key.get_pressed()
    background.display()
    player.move(pressed_key)
    player.display(window)
    player_shoot.emit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()


