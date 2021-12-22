from sprites import Sprites
from pygame import transform


class Images():
    def __init__(self, sprite_sheet, ship):
        # Player
        self.moving_forward_frames = []
        self.moving_left_frames = []
        self.moving_right_frames = []
        self.idle_frames = []
        if ship == 1:
            for i in range(0, 5):
                frame = Sprites(sprite_sheet).get_image(64 * i, 64 * 0, 64, 64)
                self.moving_forward_frames.append(frame)
            for i in range(0, 5):
                frame = Sprites(sprite_sheet).get_image(64 * i, 64 * 1, 64, 64)
                self.moving_left_frames.append(frame)
            for i in range(0, 5):
                frame = Sprites(sprite_sheet).get_image(64 * i, 64 * 2, 64, 64)
                self.moving_right_frames.append(frame)
            for i in range(3):
                frame = Sprites(sprite_sheet).get_image(0, 64 * i, 64, 64)
                self.idle_frames.append(frame)
        if ship == 2:
            for i in range(0, 6):
                frame = Sprites(sprite_sheet).get_image(64 * i, 64 * 3, 64, 64)
                self.moving_forward_frames.append(frame)
            for i in range(0, 6):
                frame = Sprites(sprite_sheet).get_image(64 * i, 64 * 4, 64, 64)
                self.moving_left_frames.append(frame)
            for i in range(0, 6):
                frame = Sprites(sprite_sheet).get_image(64 * i, 64 * 5, 64, 64)
                self.moving_right_frames.append(frame)
            for i in range(1):
                frame = Sprites(sprite_sheet).get_image(0, 64 * 3, 64, 64)
                self.idle_frames.append(frame)
                self.idle_frames.append(frame)
                self.idle_frames.append(frame)

        self.ship_frames = [Sprites(sprite_sheet).get_image(0, 0, 64, 64), Sprites(sprite_sheet).get_image(0, 64 * 3, 64, 64),
                            Sprites(sprite_sheet).get_image(64 * 6, 0, 64, 64)]

        # Explosions
        self.explosion_frames = {'tiny': [], 'small': [],
                                 'med': [], 'large': [], 'huge': [], 'massive': [], 'shield': []}
        for j in range(6, 8):
            for i in range(7):
                frame = Sprites(sprite_sheet).get_image(64 * i, 64 * j, 64, 64)
                frame_tiny = transform.scale(frame, (16, 16))
                frame_small = transform.scale(frame, (32, 32))
                frame_med = frame
                frame_large = transform.scale(frame, (128, 128))
                frame_huge = transform.scale(frame, (256, 256))
                frame_massive = transform.scale(frame, (512, 512))
                self.explosion_frames['tiny'].append(frame_tiny)
                self.explosion_frames['small'].append(frame_small)
                self.explosion_frames['med'].append(frame_med)
                self.explosion_frames['large'].append(frame_large)
                self.explosion_frames['huge'].append((frame_huge))
                self.explosion_frames['massive'].append((frame_massive))
                if j == 7 and i == 3:
                    break
        for i in range(0, 6):
            frame_shield = Sprites(sprite_sheet).get_image(64 * i, 64 * 9, 64, 64)
            self.explosion_frames['shield'].append((frame_shield))

        # Bullets
        if ship == 1:
            self.bullet_frames = [Sprites(sprite_sheet).get_image(0, 64 * 8, 32, 32)]
        if ship == 2:
            self.bullet_frames = [Sprites(sprite_sheet).get_image(32, 64 * 8, 32, 32)]

        # Powerups
        self.powerup_frames = {'bullet_speed_up': [],
                               'bullet_speed_down': [], 'ship_speed_up': [], 'ship_speed_down': []}
        frame_bspeed_up = Sprites(sprite_sheet).get_image(64, 64 * 8, 32, 32)
        frame_bspeed_down = Sprites(sprite_sheet).get_image(64 + 32, 64 * 8, 32, 32)
        frame_sspeed_up = Sprites(sprite_sheet).get_image(64, 64 * 8 + 32, 32, 32)
        frame_sspeed_down = Sprites(sprite_sheet).get_image(64 + 32, 64 * 8 + 32, 32, 32)
        self.powerup_frames['bullet_speed_up'].append((frame_bspeed_up))
        self.powerup_frames['bullet_speed_down'].append((frame_bspeed_down))
        self.powerup_frames['ship_speed_up'].append((frame_sspeed_up))
        self.powerup_frames['ship_speed_down'].append((frame_sspeed_down))

        # Asteroids
        self.asteroid_frames = [Sprites(sprite_sheet).get_image(277, 469, 22, 22),
                                Sprites(sprite_sheet).get_image(332, 465, 40, 30),
                                Sprites(sprite_sheet).get_image(384, 448, 64, 64)]
        self.asteroid_frames[0] = transform.scale(self.asteroid_frames[0], (33, 33))
        self.asteroid_frames[1] = transform.scale(self.asteroid_frames[1], (60, 45))
        self.asteroid_frames[2] = transform.scale(self.asteroid_frames[2], (96, 96))

        # Invisible Wall
        self.wall_frame = [Sprites(sprite_sheet).get_image(64 * 6, 64 * 1, 64 * 6, 10)]
        self.wall_frame[0] = transform.scale(self.wall_frame[0], (576, 10))

        # Help Icon
        self.help_frame = [Sprites(sprite_sheet).get_image(64 * 2, 64 * 8, 64, 64)]
        self.help_frame[0] = transform.scale(self.help_frame[0], (64, 64))
