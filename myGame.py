from config import *
from Background import *
from ShootingSystem import *
import Collision_Detector


def aircraft_battle():
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

    # set BGM
    pygame.mixer.init()
    pygame.mixer.music.load(BGM_PATH)
    pygame.mixer.music.set_volume(BGM_VOLUME)
    pygame.mixer.music.play(-1)

    # set a cartridge for player
    bullets = [Bullet(PLAYER_BULLET_IMG_PATH, PLAYER_BULLET_SPEED) for _ in range(BULLET_CARTRIDGE)]

    # set enemies
    enemies = [Enemy(ENEMY_IMG_PATH, ENEMY_SPEED) for _ in range(MAX_ENEMY)]
    enemy_sys = EnemySystem(enemies, window, ENEMY_INTERVAL)

    # set bombs
    bombs = [Collision_Detector.Bomb(BOMB_IMG_PATHS, BOMB_INTERVAL, window)
             for _ in range(MAX_BOMB)]

    # set player's shooting system
    player_shoot = Shooting(bullets, PLAYER_BULLET_INTERVAL, player, window, SHOOT_KEY)

    # set the running loop
    running = True
    while running:
        clock.tick(FRAMES_PER_SEC)
        pressed_key = pygame.key.get_pressed()
        background.display()
        player.move(pressed_key)
        player.display(window)
        enemy_sys.start_system()
        player_shoot.manually_launch(pressed_key)
        for enemy in enemies:
            if not enemy.isFree:
                running = Collision_Detector.enemy_player(enemy, player)
                if not running:
                    break
                # If you do not add these two lines,
                # Player will check with the other Enemy and change the value of running again
                for bullet in bullets:
                    if not bullet.isFree:
                        Collision_Detector.enemy_bullet(enemy, bullet, bombs)
        for bomb in bombs:
            bomb.update_info()
            bomb.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()
    pygame.quit()
