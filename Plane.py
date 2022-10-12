from ShootingSystem import *
from config import *
import random


# Make the shooting system a member of the player and enemy aircraft class for easy follow-up management
class Plane:
    def __init__(self, plane_path, window: pygame.Surface, bullet_path, bullet_speed, cartridge, intervals):
        # image refers to the image path of the plane
        self.image = pygame.image.load(plane_path)
        self.rect = self.image.get_rect()
        self.window = window
        self.shooting = Shooting(bullet_path, bullet_speed, cartridge, intervals)

    # display the plane on the screen
    def display(self):
        self.window.blit(self.image, (self.rect.x, self.rect.y))


class Player(Plane):
    def __init__(self, window: pygame.Surface, plane_path, speed, bullet_path, bullet_speed, cartridge,
                 intervals):
        Plane.__init__(self, plane_path, window, bullet_path, bullet_speed, cartridge, intervals)
        self.speed = speed
        # set the initial position
        self.rect.x = SCREEN_WIDTH / 3
        self.rect.y = SCREEN_HEIGHT * 2 / 3

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

    # find an available bullet and initialize it
    def __init_bullet(self):
        for bullet in self.shooting.bullets:
            if bullet.isFree:
                bullet.rect.y = self.rect.y - bullet.rect.height
                bullet.rect.x = self.rect.center[0] - bullet.rect.width/2
                bullet.isFree = False
                break

    # shoot bullet in every interval time, and update every bullet on the window
    def auto_emit(self):
        if self.shooting.cnt == self.shooting.intervals:
            self.__init_bullet()
            self.shooting.cnt = 0
        for bullet in self.shooting.bullets:
            bullet.move(self.window)
        self.shooting.cnt += 1

    # player can shoot bullet by clicking or pressing keys
    def manually_launch(self, pressed_keys, shoot_key):
        if pressed_keys[shoot_key]:
            if self.shooting.cnt >= self.shooting.intervals:
                self.__init_bullet()
                self.shooting.cnt = 0
            self.shooting.cnt += 1
        else:
            self.shooting.cnt = self.shooting.intervals
        for bullet in self.shooting.bullets:
            bullet.move(self.window)


class Enemy(Plane):
    def __init__(self, img_path, speed, window: pygame.Surface, bullet_path, bullet_speed, cartridge, intervals):
        Plane.__init__(self, img_path, window, bullet_path, bullet_speed, cartridge, intervals)
        self.isFree = True
        self.speed = speed

    def moving(self):
        if not self.isFree:
            self.rect.y += self.speed
            if self.rect.y > SCREEN_HEIGHT:
                self.isFree = True

    def __init_bullet(self):
        for bullet in self.shooting.bullets:
            if bullet.isFree:
                bullet.rect.y = self.rect.y + self.rect.height
                bullet.rect.x = self.rect.center[0] - bullet.rect.width/2
                bullet.isFree = False
                break

    # shoot bullet in every interval time, and update every bullet on the window
    def auto_emit(self):
        if self.shooting.cnt >= self.shooting.intervals:
            self.__init_bullet()
            self.shooting.cnt = 0
        self.shooting.cnt += 1


class EnemySystem:
    def __init__(self, enemies: list[Enemy], interval):
        self.enemies = enemies
        self.interval = interval
        self.cnt = 0

    def __init_enemy(self):
        for enemy in self.enemies:
            if enemy.isFree:
                enemy.rect.x = random.randint(0, SCREEN_WIDTH - enemy.rect.width)
                enemy.rect.y = ENEMY_STARTING
                enemy.isFree = False
                break

    def start_system(self):
        if self.cnt >= self.interval:
            self.__init_enemy()
            self.cnt = 0
        for enemy in self.enemies:
            if not enemy.isFree:
                enemy.display()
                enemy.auto_emit()
            # The firing logic is separated from the display logic of the
            # bullet to achieve the effect that the bullet is still present
            # after the enemy plane is dead
            for bullet in enemy.shooting.bullets:
                bullet.move(enemy.window, False)
            enemy.moving()
        self.cnt += 1

    def clear_sys(self):
        for enemy in self.enemies:
            enemy.isFree = True
            for bullet in enemy.shooting.bullets:
                bullet.isFree = True
