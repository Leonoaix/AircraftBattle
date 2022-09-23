from Background import *
from Plane import *
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

    # set game background
    background = Background(GAME_BG_PATH, GAME_BG_SPEED, window)

    # set BGM
    pygame.mixer.init()
    pygame.mixer.music.load(BGM_PATH)
    pygame.mixer.music.set_volume(BGM_VOLUME)
    pygame.mixer.music.play(-1)

    # set player
    player = Player(window, PLAYER_IMG_PATH, PLAYER_SPEED, PLAYER_BULLET_IMG_PATH, PLAYER_BULLET_SPEED,
                    BULLET_CARTRIDGE, PLAYER_BULLET_INTERVAL)

    # set enemies
    enemies = [Enemy(ENEMY_IMG_PATH, ENEMY_SPEED, window, ENEMY_BULLET_PATH, ENEMY_BULLET_SPEED, BULLET_CARTRIDGE,
                     ENEMY_BULLET_INTERVAL) for _ in range(MAX_ENEMY)]
    enemy_sys = EnemySystem(enemies, ENEMY_INTERVAL)

    # set bombs
    bombs = [Collision_Detector.Bomb(BOMB_IMG_PATHS, BOMB_INTERVAL, window)
             for _ in range(MAX_BOMB)]

    # set the running loop
    running = True
    while running:
        clock.tick(FRAMES_PER_SEC)
        pressed_key = pygame.key.get_pressed()
        background.display()
        player.move(pressed_key)
        player.display()
        player.manually_launch(pressed_key, pygame.K_SPACE)
        enemy_sys.start_system()
        for enemy in enemies:
            if not enemy.isFree:
                running = Collision_Detector.enemy_player(enemy, player)
                if not running:
                    break
                for bullet in enemy.shooting.bullets:
                    running = Collision_Detector.bullet_player(bullet, player)
                    if not running:
                        break
                if not running:
                    break
                # If you do not add these two lines,
                # Player will check with the other Enemy and change the value of running again
                for bullet in player.shooting.bullets:
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
