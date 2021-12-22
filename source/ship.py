import pygame
from bullet import Bullet
from math import sqrt
vec = pygame.math.Vector2


class Ship(pygame.sprite.Sprite):
    def __init__(self, game_settings, sprite_group, images, shot_sound, reload_sound):
        # Initialize sprite
        pygame.sprite.Sprite.__init__(self)
        self.sprite_group = sprite_group
        self.image = images.idle_frames[0]
        self.rect = self.image.get_rect()
        self.last_update = 0
        self.current_frame = 0
        self.shots = 0
        self.last_shot = pygame.time.get_ticks()
        self.last_reload = pygame.time.get_ticks()
        self.alive = True
        self.reloading = False
        self.shot_sound = shot_sound

        if game_settings.ship == 1:
            self.reload_sound = reload_sound[0]
            self.shield = 25
        if game_settings.ship == 2:
            self.reload_sound = reload_sound[1]
            self.shield = 100
        self.health = 100
        self.bullets = game_settings.bullets_allowed - self.shots

        # Initialize vectors
        self.pos = vec(game_settings.screen_width / 2,
                       game_settings.screen_height - self.rect.height)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def update(self, game_settings, images):
        keys = pygame.key.get_pressed()
        self.animate(keys, images)
        self.get_speed(game_settings, keys)
        # Shoot bullets
        if keys[pygame.K_SPACE] and self.alive:
            self.shoot(game_settings, self.sprite_group.all_sprites,
                       self.sprite_group.bullets, images, keys)

        # Reload
        now = pygame.time.get_ticks()
        if (self.shots == game_settings.bullets_allowed and not self.reloading) or (keys[pygame.K_r] and self.shots != 0 and not self.reloading)\
                and self.alive:
            if game_settings.ship == 1:
                self.reload_sound.play(game_settings.bullets_allowed - 1)
            if game_settings.ship == 2:
                self.reload_sound.play()
            self.reloading = True
            self.last_reload = now
            self.shots = game_settings.bullets_allowed + 1
            self.bullets = game_settings.bullets_allowed - self.shots
            if self.shots == game_settings.bullets_allowed + 1:
                self.bullets = 0
        if now - self.last_reload > game_settings.reload_time and self.shots > game_settings.bullets_allowed\
                and self.alive:
            self.last_reload = now
            self.reloading = False
            self.shots = 0
            self.bullets = game_settings.bullets_allowed

    def get_speed(self, game_settings, keys):
        self.acc = vec(0, 0)

        if (keys[pygame.K_LEFT] and keys[pygame.K_UP]) or (keys[pygame.K_LEFT] and keys[pygame.K_DOWN])\
           or (keys[pygame.K_RIGHT] and keys[pygame.K_UP]) or (keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]):
            ship_acc = sqrt(2) * game_settings.ship_acc / 2
        else:
            ship_acc = game_settings.ship_acc

        if keys[pygame.K_LEFT] and self.pos.x > game_settings.screen_rect.left + self.rect.width:
            self.acc.x = -ship_acc
            if keys[pygame.K_RIGHT]:
                self.acc.x = 0

        if keys[pygame.K_RIGHT] and self.pos.x < game_settings.screen_rect.right - self.rect.width:
            self.acc.x = ship_acc
            if keys[pygame.K_LEFT]:
                self.acc.x = 0

        if keys[pygame.K_UP] and self.pos.y > game_settings.screen_rect.top + self.rect.height:
            self.acc.y = -ship_acc
            if keys[pygame.K_DOWN]:
                self.acc.y = 0
        if keys[pygame.K_DOWN] and self.pos.y < game_settings.screen_rect.bottom - self.rect.height:
            self.acc.y = ship_acc
            if keys[pygame.K_UP]:
                self.acc.y = 0

        # Update vectors
        self.acc += self.vel * game_settings.ship_fric
        self.vel += self.acc
        if -0.08 < self.vel.x < 0.08:
            self.vel.x = 0
        if -0.08 < self.vel.y < 0.08:
            self.vel.y = 0
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

        # Screen boundaries
        if self.pos.x < game_settings.screen_rect.left + self.rect.width / 2 and self.alive:
            self.pos.x = game_settings.screen_rect.left + self.rect.width / 2
            self.vel.x = 0.5
        if self.pos.x > game_settings.screen_rect.right - self.rect.width / 2 and self.alive:
            self.pos.x = game_settings.screen_rect.right - self.rect.width / 2
            self.vel.x = -0.5
        if self.pos.y < game_settings.screen_rect.top + self.rect.height / 2 and self.alive:
            self.pos.y = game_settings.screen_rect.top + self.rect.height / 2
            self.vel.y = 0.5
        if self.pos.y > game_settings.screen_rect.bottom - self.rect.height / 2 and self.alive:
            self.pos.y = game_settings.screen_rect.bottom - self.rect.height / 2
            self.vel.y = -0.5

    def shoot(self, game_settings, all_sprites, bullets, images, keys):
        # Spawn bullets
        now = pygame.time.get_ticks()
        if now - self.last_shot > game_settings.bullet_delay and self.shots < game_settings.bullets_allowed:
            self.shots += 1
            self.bullets = game_settings.bullets_allowed - self.shots
            self.last_shot = now
            self.shot_sound.play()
            bullet = Bullet(game_settings, self.rect.centerx, self.rect.top, images.bullet_frames)
            all_sprites.add(bullet)
            bullets.add(bullet)

    def animate(self, keys, images):
        now = pygame.time.get_ticks()

        if (keys[pygame.K_UP] and keys[pygame.K_DOWN] and keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            if now - self.last_update > 150:
                self.last_update = now
                self.image = images.moving_forward_frames[self.current_frame]
                self.current_frame += 1
                if self.current_frame == 4:
                    self.current_frame = 0

        elif keys[pygame.K_LEFT] and keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            if now - self.last_update > 150:
                self.last_update = now
                self.image = images.moving_left_frames[self.current_frame]
                self.current_frame += 1
                if self.current_frame == 4:
                    self.current_frame = 0

        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            if now - self.last_update > 150:
                self.last_update = now
                self.image = images.moving_right_frames[self.current_frame]
                self.current_frame += 1
                if self.current_frame == 4:
                    self.current_frame = 0

        elif keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            self.image = images.idle_frames[0]
        elif (keys[pygame.K_UP] and keys[pygame.K_DOWN]) or\
             (keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] and not keys[pygame.K_UP]):
            if now - self.last_update > 150:
                self.last_update = now
                self.image = images.moving_forward_frames[self.current_frame]
                self.current_frame += 1
                if self.current_frame == 4:
                    self.current_frame = 0

        elif ((keys[pygame.K_LEFT] and keys[pygame.K_DOWN]) or (keys[pygame.K_RIGHT] and keys[pygame.K_DOWN])
              and not keys[pygame.K_UP]):
            if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
                self.image = images.idle_frames[1]
            elif keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
                self.image = images.idle_frames[2]

        elif keys[pygame.K_UP] and keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            if now - self.last_update > 100:
                self.last_update = now
                self.image = images.moving_forward_frames[self.current_frame]
                self.current_frame += 1
                if self.current_frame == 4:
                    self.current_frame = 0

        elif keys[pygame.K_LEFT]:
            if keys[pygame.K_UP]:
                if now - self.last_update > 100:
                    self.last_update = now
                    self.image = images.moving_left_frames[self.current_frame]
                    self.current_frame += 1
                    if self.current_frame == 4:
                        self.current_frame = 0
            else:
                if now - self.last_update > 150:
                    self.last_update = now
                    self.image = images.moving_left_frames[self.current_frame]
                    self.current_frame += 1
                    if self.current_frame == 4:
                        self.current_frame = 0

        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_UP]:
                if now - self.last_update > 100:
                    self.last_update = now
                    self.image = images.moving_right_frames[self.current_frame]
                    self.current_frame += 1
                    if self.current_frame == 4:
                        self.current_frame = 0
            else:
                if now - self.last_update > 150:
                    self.last_update = now
                    self.image = images.moving_right_frames[self.current_frame]
                    self.current_frame += 1
                    if self.current_frame == 4:
                        self.current_frame = 0

        elif keys[pygame.K_UP]:
            if now - self.last_update > 100:
                self.last_update = now
                self.image = images.moving_forward_frames[self.current_frame]
                self.current_frame += 1
                if self.current_frame == 4:
                    self.current_frame = 0

        elif keys[pygame.K_DOWN]:
            self.image = images.idle_frames[0]
        else:
            if now - self.last_update > 150:
                self.last_update = now
                self.image = images.moving_forward_frames[self.current_frame]
                self.current_frame += 1
                if self.current_frame == 4:
                    self.current_frame = 0

        self.mask = pygame.mask.from_surface(self.image)
