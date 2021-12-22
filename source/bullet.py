import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game_settings, x, y, bullet_frames):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_frames[0]
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -game_settings.bullet_speed_factor

    def update(self, game_settings, images):
        self.rect.y += self.speedy
        self.mask = pygame.mask.from_surface(self.image)

        if self.rect.bottom < 0:
            self.kill()
