import pygame


# The idea behind scrolling is to alternate between two images
class Background:
    def __init__(self, image, speed, window):
        self.image1 = pygame.image.load(image)
        self.image2 = pygame.image.load(image)
        self.speed = speed
        self.window = window
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect2.y -= self.rect1.height

    # display the background, can set static or scrolling mode
    def display(self, is_scroll=True):
        if is_scroll:
            self.rect1.y += self.speed
            self.rect2.y += self.speed
            self.window.blit(self.image1, self.rect1)
            self.window.blit(self.image2, self.rect2)
            if self.rect1.y == self.image1.get_height():
                self.rect1.y = -self.rect1.y
            if self.rect2.y == self.image1.get_height():
                self.rect2.y = -self.rect2.y
        else:
            self.window.blit(self.image1, (0, 0))
