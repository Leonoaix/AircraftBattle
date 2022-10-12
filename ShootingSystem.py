import pygame
from config import SCREEN_HEIGHT

class Bullet:
    def __init__(self, img_path, speed):
        # initialize the bullet's speed (the pxs moved every time)
        self.speed = speed
        # loading the bullet's image
        self.image = pygame.image.load(img_path)
        # shows if this bullet is available
        self.isFree = True
        # get rectangle area for bullet
        self.rect = self.image.get_rect()

    # shoot on a line
    def update_position(self, upward):
        if upward:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        if self.rect.y < 0 or self.rect.y > SCREEN_HEIGHT:
            self.isFree = True

    # if bullet is on the window, display it
    def move(self, screen: pygame.Surface, upward=True):
        if not self.isFree:
            screen.blit(self.image, self.rect)
            self.update_position(upward)


class Shooting:
    def __init__(self, bullet_path, bullet_speed, cartridge, intervals):
        self.bullets = [Bullet(bullet_path, bullet_speed) for _ in range(cartridge)]
        self.intervals = intervals
        self.cnt = 0

    def clear(self):
        for bullet in self.bullets:
            bullet.isFree = True
