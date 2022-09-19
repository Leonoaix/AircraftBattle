import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT


class Plane:
    def __init__(self, image):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def display(self, window: pygame.Surface):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Plane):
    def __init__(self, image: pygame.Surface, speed):
        Plane.__init__(self, image)
        self.speed = speed
        self.rect.x = SCREEN_WIDTH/3
        self.rect.y = SCREEN_HEIGHT*2/3

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.x -= self.speed
        if pressed_key[pygame.K_RIGHT] and self.rect.x + self.image.get_width() + self.speed <= SCREEN_WIDTH:
            self.rect.x += self.speed
        if pressed_key[pygame.K_UP] and self.rect.y - self.speed >= 0:
            self.rect.y -= self.speed
        if pressed_key[pygame.K_DOWN] and self.rect.y + self.speed + self.image.get_height() <= SCREEN_HEIGHT:
            self.rect.y += self.speed

