import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, game_settings, images):
        # Initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = images.wall_frame[0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        # Initialize position
        self.rect.centerx = game_settings.screen_width / 2
        self.rect.y = game_settings.screen_height + 100
