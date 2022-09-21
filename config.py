# All speed means how many pixels an object moves per frame

FRAMES_PER_SEC = 100
SCREEN_WIDTH = 512
SCREEN_HEIGHT = 768
GAME_NAME = "Aircraft Battle v.1.0"
ICON_PATH = "res/app.ico"

GAME_BG_PATH = "res/img_bg_level_1.jpg"
GAME_BG_SPEED = 1

BGM_PATH = "res/bg.wav"

PLAYER_IMG_PATH = "res/hero2.png"
PLAYER_SPEED = 2

ENEMY_IMG_PATH = "res/img-plane_1.png"
ENEMY_SPEED = 2
MAX_ENEMY = 15
ENEMY_INTERVAL = 50

BULLET_CARTRIDGE = 15
PLAYER_BULLET_IMG_PATH = "res/hero_bullet_7.png"
PLAYER_BULLET_SPEED = 2
PLAYER_BULLET_INTERVAL = FRAMES_PER_SEC / 2

BOMB_IMG_PATHS = ["res/bomb-1.png", "res/bomb-2.png", "res/bomb-3.png",
                  "res/bomb-4.png", "res/bomb-5.png", "res/bomb-6.png", "res/bomb-7.png"]
BOMB_INTERVAL = 8
MAX_BOMB = 20
