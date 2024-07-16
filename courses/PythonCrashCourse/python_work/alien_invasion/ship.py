import pygame
from pygame.sprite import Sprite
from settings import Settings


class Ship(Sprite):
    # TODO: allow ship to move to half to the bottom screen
    def __init__(self, ai_game, is_score=False) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.settings: Settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = self._check_if_score(is_score)
        self.rect = self.image.get_rect()
        self.center_ship()
        self.moving_right = False
        self.moving_left = False

    def _check_if_score(self, is_score):
        if is_score:
            return pygame.transform.grayscale(
                pygame.transform.scale_by(
                    pygame.image.load("images/ship.png"), 0.5
                )
            )
        else:
            return pygame.image.load("images/ship.png")


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        self.rect.x = int(self.x)
        # print(f"x:{self.rect.x}")

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
