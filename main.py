import pygame.draw

from Background import *
from Plane import *
import Collision_Detector
from enum import Enum
import Button


def main():
    pygame.init()

    class Pages(Enum):
        MAIN_MENU = 1
        GAME_PAGE = 2
        SCORING_PAGE = 3

    current_page = Pages['MAIN_MENU']

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

    # add a start button on the main screen
    start_button = Button.Button(START_BTN, window)

    # add a button for returning to main menu
    ret_btn = Button.Button(RET_BUTTON, window)

    # add a score variable for storing scores
    score = 0

    # set the font for showing score
    font = pygame.font.Font(SCORING_FONT_PATH, SCORING_FONT_SIZE)

    # set the running loop
    running = True
    while running:
        clock.tick(FRAMES_PER_SEC)
        mouse_pos = pygame.mouse.get_pos()
        mouse_button = pygame.mouse.get_pressed()[0]
        if current_page == Pages['GAME_PAGE']:
            pressed_key = pygame.key.get_pressed()
            background.display()
            player.move(pressed_key)
            player.display()
            player.manually_launch(pressed_key, pygame.K_SPACE)
            enemy_sys.start_system()
            text = font.render("score: %d" % score, True, 'white')
            window.blit(text, (0, 0))
            for enemy in enemies:
                for bullet in enemy.shooting.bullets:
                    if not bullet.isFree:
                        if Collision_Detector.bullet_player(bullet, player):
                            current_page = Pages['SCORING_PAGE']
                            break
                # If you do not add these two lines,
                # Player will check with the other Enemy and change the value of running again
                if current_page == Pages['SCORING_PAGE']:
                    break
                if not enemy.isFree:
                    if Collision_Detector.enemy_player(enemy, player):
                        current_page = Pages['SCORING_PAGE']
                        break
                    for bullet in player.shooting.bullets:
                        if not bullet.isFree:
                            score += Collision_Detector.enemy_bullet(enemy, bullet, bombs)
            for bomb in bombs:
                bomb.update_info()
                bomb.show()
        elif current_page == Pages['MAIN_MENU']:
            background.display(False)
            start_button.show(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
            if start_button.clicked(mouse_pos, mouse_button):
                current_page = Pages['GAME_PAGE']
        elif current_page == Pages["SCORING_PAGE"]:
            background.display(False)
            surface = pygame.image.load(SCORING_WINDOW)
            window.blit(surface, (SCORING_WINDOW_X, SCORING_WINDOW_Y))
            start_button.show(SCORING_START_X, SCORING_START_Y)
            ret_btn.show(SCORING_BACK_X, SCORING_BACK_Y)
            text = font.render("score: %d" % score, True, 'black')
            window.blit(text, (SCORING_X, SCORING_Y))
            if start_button.clicked(mouse_pos, mouse_button):
                score = 0
                enemy_sys.clear_sys()
                player.shooting.clear()
                for bomb in bombs:
                    bomb.clear()
                current_page = Pages['GAME_PAGE']
            if ret_btn.clicked(mouse_pos, mouse_button):
                score = 0
                enemy_sys.clear_sys()
                player.shooting.clear()
                for bomb in bombs:
                    bomb.clear()
                current_page = Pages['MAIN_MENU']
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()


if __name__ == "__main__":
    main()

