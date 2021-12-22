import pygame
import random
from random import choices


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, game_settings, rand_val, images):
        # Initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.image_original = images.asteroid_frames[rand_val[0]]
        self.image = self.image_original.copy()
        self.rect = self.image.get_rect()
        self.rect_original = self.image_original.get_rect()

        # Initialize position
        self.rect.x = random.randrange(0, game_settings.screen_width - self.rect.width)
        self.rect.y = random.randrange(2 * (-self.rect.height - 10), -self.rect.height - 10)
        self.speedx = random.randrange(-2, 3)
        self.speedy = random.randrange(1, 5)

        # Initialize rotation
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_original, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
            self.mask = pygame.mask.from_surface(self.image)

    def update(self, game_settings, images):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Respawn at the top
        if (self.rect.left < -self.rect.width) or\
           (self.rect.right > game_settings.screen_width + self.rect.width):
            rand_val = choices([0, 1, 2])
            self.image_original = images.asteroid_frames[rand_val[0]]
            self.image = self.image_original.copy()
            self.rect = self.image.get_rect()
            self.rect_original = self.image_original.get_rect()
            self.rect.x = random.randrange(0, game_settings.screen_width - self.rect.width)
            self.rect.y = random.randrange(2 * (-self.rect.height - 10), -self.rect.height - 10)
            self.speedy = random.randrange(1, 5)
            self.speedx = random.randrange(-2, 3)
