from ShootingSystem import Enemy, Bullet, pygame, Player
from config import BOMB_SOUND_PATH, BOMB_VOLUME

pygame.mixer.init()
bomb_sound = pygame.mixer.Sound(BOMB_SOUND_PATH)
bomb_sound.set_volume(BOMB_VOLUME)


class Bomb:
    def __init__(self, images: list[str], interval, window: pygame.Surface):
        self.images = [pygame.image.load(image) for image in images]
        self.interval = interval
        self.window = window
        self.x = self.y = 0
        self.isFree = True
        self.cnt = 0
        self.index = 0

    # Control switching diagram
    def update_info(self):
        if not self.isFree:
            self.cnt += 1
            if self.cnt == self.interval:
                self.index += 1
                if self.index == len(self.images):
                    self.index = 0
                    self.isFree = True
                self.cnt = 0

    def show(self):
        if not self.isFree:
            self.window.blit(self.images[self.index], (self.x, self.y))


def enemy_bullet(enemy: Enemy, bullet: Bullet, bombs: list[Bomb]):
    if enemy.rect.colliderect(bullet.rect):
        bullet.isFree = True
        enemy.isFree = True
        for bomb in bombs:
            if bomb.isFree:
                bomb.x = enemy.rect.x
                bomb.y = enemy.rect.y
                bomb.isFree = False
                bomb_sound.play()
                break


def enemy_player(enemy: Enemy, player: Player):
    if enemy.rect.colliderect(player.rect):
        return False
    return True
