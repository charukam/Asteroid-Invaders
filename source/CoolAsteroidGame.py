import pygame
from settings import Settings
from ship import Ship
from asteroid import Asteroid
from wall import Wall
import draw_background as draw_bg
from game_over_screen import game_over_screen
import check_collisions as collisions
from sprites import Sprites
from load_images import Images
from drawText import drawText
from drawHUD import drawHUD
from random import choices
from os import path


# Initialize pygame and create window
pygame.mixer.pre_init(44100, -16, 1, 1024)
pygame.init()
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()
HIGHSCORE_FILE = "highscore.txt"
game_settings = Settings()
try:
    with open(path.join(path.dirname(__file__), HIGHSCORE_FILE), 'r') as file:
        game_settings.highscore = int(file.read())
except Exception:
    with open(path.join(path.dirname(__file__), HIGHSCORE_FILE), 'w') as file:
        game_settings.highscore = 0

# Load images
sprite_sheet = pygame.image.load('sprite_sheet.png').convert_alpha()
background = pygame.image.load('background.bmp').convert_alpha()
bg_par1 = pygame.image.load('bg_par1.bmp').convert_alpha()
bg_par2 = pygame.image.load('bg_par2.bmp').convert_alpha()
bg_par3 = pygame.image.load('bg_par3.bmp').convert_alpha()
bg_rect = background.get_rect()
background_images = [background, bg_par1, bg_par2, bg_par3, bg_rect]

# Load sounds
shot_sound = pygame.mixer.Sound('shot.wav')
reload_sound = [pygame.mixer.Sound('reload1.wav'),
                pygame.mixer.Sound('reload2.wav')]
explode_sounds = []
for sound in ['explosion1.wav', 'explosion2.wav']:
    explode_sounds.append(pygame.mixer.Sound(sound))
ship_explode_sound = pygame.mixer.Sound('ship_explode.wav')
powerup_sound = pygame.mixer.Sound('powerup.wav')
select_sound = pygame.mixer.Sound('select.wav')
pygame.mixer.music.load('Blue Space v0_96.wav')
pygame.mixer.music.set_volume(game_settings.music_level)
shot_sound.set_volume(game_settings.sound_level)
reload_sound[0].set_volume(game_settings.sound_level)
reload_sound[1].set_volume(game_settings.sound_level)
powerup_sound.set_volume(game_settings.sound_level / 4)
explode_sounds[0].set_volume(game_settings.sound_level)
explode_sounds[1].set_volume(game_settings.sound_level)
ship_explode_sound.set_volume(game_settings.sound_level)
select_sound.set_volume(game_settings.sound_level / 4)
pygame.mixer.music.play(loops=-1)

# Initialize all the sprites
sprite_group = Sprites(sprite_sheet)
images = Images(sprite_sheet, game_settings.ship)
sprite_group.all_sprites = pygame.sprite.Group()
sprite_group.mobs = pygame.sprite.Group()
sprite_group.bullets = pygame.sprite.Group()
sprite_group.powerups = pygame.sprite.Group()
player = Ship(game_settings, sprite_group, images, shot_sound, reload_sound)
wall_sprite = Wall(game_settings, images)
mob_count = 2
for i in range(mob_count):
    rand_val = choices([0, 1, 2])
    asteroid = Asteroid(game_settings, rand_val, images)
    sprite_group.mobs.add(asteroid)
    sprite_group.all_sprites.add(asteroid)
sprite_group.all_sprites.add(player)
sprite_group.all_sprites.add(wall_sprite)

# Initialize variables
background_speed = 1

# Game loop
running = True

while running:
    if game_settings.game_over:
        draw_bg.DrawBackground(game_settings.screen, background_images,
                               player, background_speed)
        game_settings = Settings()
        game_over_screen(game_settings, images, background_images,
                         player, background_speed, select_sound)

        try:
            with open(path.join(path.dirname(__file__), HIGHSCORE_FILE), 'r') as file:
                game_settings.highscore = int(file.read())
        except Exception:
            with open(path.join(path.dirname(__file__), HIGHSCORE_FILE), 'w') as file:
                game_settings.highscore = 0

        # Initialize all the sprites
        sprite_group = Sprites(sprite_sheet)
        images = Images(sprite_sheet, game_settings.ship)
        sprite_group.all_sprites = pygame.sprite.Group()
        sprite_group.mobs = pygame.sprite.Group()
        sprite_group.bullets = pygame.sprite.Group()
        sprite_group.powerups = pygame.sprite.Group()
        player = Ship(game_settings, sprite_group, images, shot_sound, reload_sound)
        wall_sprite = Wall(game_settings, images)
        mob_count = 2
        for i in range(mob_count):
            rand_val = choices([0, 1, 2])
            asteroid = Asteroid(game_settings, rand_val, images)
            sprite_group.mobs.add(asteroid)
            sprite_group.all_sprites.add(asteroid)
        sprite_group.all_sprites.add(player)
        sprite_group.all_sprites.add(wall_sprite)
        game_settings.game_over = False

    # keep loop running at the right speed
    clock.tick(game_settings.FPS)
    now = pygame.time.get_ticks()

    # Process input (events)
    for event in pygame.event.get():
        # Check for closing window
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            running = False

    # Draw / render
    draw_bg.DrawBackground(game_settings.screen, background_images, player, background_speed)
    sprite_group.all_sprites.draw(game_settings.screen)
    drawText(game_settings.screen, 'arial bold', "Score: "
             + str(game_settings.score), 32, game_settings.screen_width / 2, 10)
    drawText(game_settings.screen, 'arial bold', "Wave: "
             + str(game_settings.wave), 32, game_settings.screen_width / 2, 50)
    drawText(game_settings.screen, 'courier', "x" + str(player.bullets), 25,
             game_settings.screen_width - 25, game_settings.screen_height - 32)
    drawHUD(game_settings.screen, 10, 10, player.shield,
            player.health, images, game_settings.ship)

    # Update
    sprite_group.all_sprites.update(game_settings, images)

    # Check collisions
    collisions.check_collisions(sprite_group, explode_sounds, images,
                                game_settings, player, ship_explode_sound, powerup_sound, wall_sprite, rand_val)

    if game_settings.score < 0:
        game_settings.score = 0
    if game_settings.wave < 1:
        game_settings.wave = 1
    if game_settings.score > game_settings.highscore:
        game_settings.highscore = game_settings.score

    with open(path.join(path.dirname(__file__), HIGHSCORE_FILE), 'w') as f:
        f.write(str(game_settings.highscore))

    # Change wave
    if len(sprite_group.mobs) == 0:
        game_settings.wave_flag = False
        if game_settings.wave_flag is False:
            if game_settings.timer_flag is False:
                game_settings.delay_time = now
                game_settings.timer_flag = True
            drawText(game_settings.screen, 'arial bold', "NEXT WAVE", 128,
                     game_settings.screen_width / 2, game_settings.screen_width / 2)
            background_speed = 10
            if now - game_settings.delay_time > 2000:
                game_settings.delay_time = now + 2000
                game_settings.wave += 1
                background_speed = 1
                for i in range(game_settings.wave * 4):
                    rand_val = choices([0, 1, 2])
                    asteroid = Asteroid(game_settings, rand_val, images)
                    sprite_group.mobs.add(asteroid)
                    sprite_group.all_sprites.add(asteroid)
                game_settings.wave_flag = True
                game_settings.timer_flag = False
    pygame.display.flip()
pygame.quit()
