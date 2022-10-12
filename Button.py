import pygame


class Button:
    # x, y represent the upper left corner of the button, and image represents the image of the button
    def __init__(self, image, window: pygame.Surface):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.is_pressed = False
        self.window = window

    # Determine whether the button is clicked by mouse_button
    def clicked(self, mouse_pos, mouse_button):
        if self.rect.collidepoint(mouse_pos):
            if mouse_button and not self.is_pressed:
                self.is_pressed = True
                self.rect.y += 5
            elif not mouse_button and self.is_pressed:
                self.is_pressed = False
                self.rect.y -= 5
                return True
        return False

    def show(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.window.blit(self.image, self.rect)
