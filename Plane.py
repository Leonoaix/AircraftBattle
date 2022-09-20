import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
import random


class Plane:
    def __init__(self, image):
        # image refers to the image path of the plane
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    # display the plane on the screen
    def display(self, window: pygame.Surface):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Plane):
    def __init__(self, image: pygame.Surface, speed):
        Plane.__init__(self, image)
        self.speed = speed
        # set the initial position
        self.rect.x = SCREEN_WIDTH/3
        self.rect.y = SCREEN_HEIGHT*2/3

    # let the plane move with direction key, and add a barrier detection
    def move(self, pressed_key):
        if pressed_key[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed
        if pressed_key[pygame.K_RIGHT] and self.rect.x + self.image.get_width() + self.speed <= SCREEN_WIDTH:
            self.rect.x += self.speed
        if pressed_key[pygame.K_UP] and self.rect.y - self.speed >= 0:
            self.rect.y -= self.speed
        if pressed_key[pygame.K_DOWN] and self.rect.y + self.speed + self.image.get_height() <= SCREEN_HEIGHT:
            self.rect.y += self.speed


class Enemy(Plane):
    def __init__(self, img_path, speed):
        Plane.__init__(self, img_path)
        self.isFree = True
        self.speed = speed

    def moving(self):
        if not self.isFree:
            self.rect.y += self.speed
            if self.rect.y > SCREEN_HEIGHT:
                self.isFree = True


class EnemySystem:
    def __init__(self, enemies: list[Enemy], screen, interval):
        self.enemies = enemies
        self.screen = screen
        self.interval = interval
        self.cnt = 0

    def __init_enemy(self):
        for enemy in self.enemies:
            if enemy.isFree:
                enemy.rect.x = random.randint(0, SCREEN_WIDTH - enemy.rect.width)
                print(enemy.rect.x)
                enemy.rect.y = 0
                enemy.isFree = False
                break

    def start_system(self):
        if self.cnt == self.interval:
            self.__init_enemy()
            self.cnt = 0
        for enemy in self.enemies:
            if not enemy.isFree:
                enemy.display(self.screen)
            enemy.moving()
        self.cnt += 1

