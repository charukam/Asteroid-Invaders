import pygame


class Settings():
    """A class to store all settings for Asteroids."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 576
        self.screen_height = 1024
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.bg_color = (40, 44, 52)
        self.FPS = 120

        # Sound Settings
        self.music_level = 0.10
        self.sound_level = 0.3

        # Ship Settings
        self.ship = 1
        self.ship_acc = 0.2
        self.ship_fric = -0.025

        # Bullet Settings
        if self.ship == 1:
            self.bullet_speed_factor = 20
            self.bullets_allowed = 4
            self.reload_time = 500 * self.bullets_allowed
            self.bullet_delay = 400
        if self.ship == 2:
            self.bullet_speed_factor = 45
            self.bullets_allowed = 10
            self.reload_time = 1770
            self.bullet_delay = 300

        # Mob settings
        self.mob_count = 2

        # Score
        self.score = 0
        self.wave = 1

        # Powerups
        self.powerup_frequency = 0.4

        # Gameover
        self.game_over = True

        # Flags
        self.wave_flag = True
        self.dead_flag = True
        self.timer_flag = False
        self.delay_time = 0
        self.delay_time2 = 0
        self.hovered = False
