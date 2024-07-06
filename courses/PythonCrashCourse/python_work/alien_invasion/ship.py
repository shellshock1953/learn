import pygame
from settings import Settings


class Ship:
    # TODO: allow ship to move to half to the bottom screen
    def __init__(self, ai_game) -> None:
        self.screen = ai_game.screen
        self.settings: Settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        self.rect.x = int(self.x)
        # print(f"x:{self.rect.x}")

    def blitme(self):
        self.screen.blit(self.image, self.rect)
