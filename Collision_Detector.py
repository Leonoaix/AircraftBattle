from ShootingSystem import Enemy, Bullet, pygame


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
                break
