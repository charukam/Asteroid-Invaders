import pygame
from random import randint


class Powerup(pygame.sprite.Sprite):
    def __init__(self, images, center, powerup_type):
        pygame.sprite.Sprite.__init__(self)
        self.type = powerup_type
        self.image = images.powerup_frames[powerup_type][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = randint(2, 4)

    def update(self, game_settings, images):
        self.rect.y += self.speedy
        self.mask = pygame.mask.from_surface(self.image)

        if self.rect.bottom > game_settings.screen_height:
            self.kill()
