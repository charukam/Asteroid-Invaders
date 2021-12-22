from drawText import drawText
from asteroid import Asteroid
from random import choices


def new_wave(sprite_group, game_settings, wave_flag, timer_flag, now, delay_time, background_speed, images):

    wave_flag = False
    if wave_flag is False:
        if timer_flag is False:
            delay_time = now
            timer_flag = True
        drawText(game_settings.screen, 'arial bold', "NEXT WAVE", 128,
                 game_settings.screen_width / 2, game_settings.screen_width / 2)
        background_speed = 10
        if now - delay_time > 5000:
            delay_time = now + 5000
            game_settings.wave += 1
            background_speed = 1
            for i in range(game_settings.wave * 4):
                rand_val = choices([0, 1, 2])
                asteroid = Asteroid(game_settings, rand_val, images)
                sprite_group.mobs.add(asteroid)
                sprite_group.all_sprites.add(asteroid)
            wave_flag = True
            timer_flag = False
    print(now, delay_time)
