import pygame
from pygame.sprite import Sprite
from settings import Settings
# from alien_invasion import AlienInvasion

class Bullet(Sprite):
    # TODO: bullets should be img
    # HERE - adding bullet as img
    def __init__(self, ai_game):
        super().__init__()

        self.settings: Settings = ai_game.settings
        # self.screen_rect = ai_game.screen.get_rect()
        self.screen = ai_game.screen
        self.color = self.settings.bullet_color
        
        self.rect = pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
