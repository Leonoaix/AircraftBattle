from Plane import *


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
    def update_position(self):
        if not self.isFree:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.isFree = True

    # if bullet is on the window, display it
    def display(self, screen: pygame.Surface):
        if not self.isFree:
            screen.blit(self.image, self.rect)


class Shooting:
    def __init__(self, bullets: list[Bullet], intervals, shooter: Plane, screen: pygame.Surface):
        self.bullets = bullets
        self.intervals = intervals
        self.shooter = shooter
        self.screen = screen
        self.__cnt = 0

    # find an available bullet and initialize it
    def __init_bullet(self):
        for bullet in self.bullets:
            if bullet.isFree:
                bullet.rect.y = self.shooter.rect.y - bullet.image.get_height()
                bullet.rect.x = self.shooter.rect.x + self.shooter.image.get_width() / 2
                bullet.isFree = False
                break

    # shoot bullet in every interval time, and update every bullet on the window
    def emit(self):
        if self.__cnt == self.intervals:
            self.__init_bullet()
            self.__cnt = 0
        for bullet in self.bullets:
            bullet.display(self.screen)
            bullet.update_position()
        self.__cnt += 1


