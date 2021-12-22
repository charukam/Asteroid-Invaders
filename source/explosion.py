import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, images, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = images.explosion_frames[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 45

    def update(self, game_settings, images):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(images.explosion_frames[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = images.explosion_frames[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
