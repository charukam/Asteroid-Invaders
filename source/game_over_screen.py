import pygame
from drawText import drawText
import draw_background as draw_bg
from os import path


def game_over_screen(game_settings, images, background_images, player, background_speed, select_sound):
    try:
        with open('highscore.txt', 'r') as file:
            game_settings.highscore = int(file.read())
    except Exception:
        with open('highscore.txt', 'w') as file:
            game_settings.highscore = 0

    ship_sprite1 = images.ship_frames[0]
    ship_sprite2 = images.ship_frames[1]
    ship_sprite_locked = images.ship_frames[2]
    help_icon = images.help_frame[0]
    bspeedup_sprite = images.powerup_frames['bullet_speed_up'][0]
    bspeeddown_sprite = images.powerup_frames['bullet_speed_down'][0]
    sspeedup_sprite = images.powerup_frames['ship_speed_up'][0]
    sspeeddown_sprite = images.powerup_frames['ship_speed_down'][0]

    if game_settings.highscore >= 4269:
        ship1_rect = ship_sprite1.get_rect()
        ship1_rect.x = 16
        ship1_rect.y = game_settings.screen_height - 64 * 3.5
    else:
        ship1_rect = ship_sprite_locked.get_rect()
        ship1_rect.x = 16
        ship1_rect.y = game_settings.screen_height - 64 * 3.5

    ship2_rect = ship_sprite2.get_rect()
    ship2_rect.x = 16
    ship2_rect.y = game_settings.screen_height - 98

    help_icon_rect = help_icon.get_rect()
    help_icon_rect.x = 12
    help_icon_rect.y = 12

    waiting = True
    while waiting:
        pygame.time.Clock().tick(game_settings.FPS)
        pygame.event.pump()

        if ship1_rect.collidepoint(pygame.mouse.get_pos()):
            draw_bg.DrawBackground(game_settings.screen, background_images,
                                   player, background_speed)
            drawText(game_settings.screen, 'comicsansms', "COOL",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2 - 100)
            drawText(game_settings.screen, 'comicsansms', "ASTEROID",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2)
            drawText(game_settings.screen, 'comicsansms', "GAME",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2 + 100)
            drawText(game_settings.screen, 'arial bold', "High Score: "
                     + str(game_settings.highscore), 24, game_settings.screen_width - 96, game_settings.screen_height - 32)
            game_settings.screen.blit(help_icon, (12, 12))
            if game_settings.highscore >= 4269:
                game_settings.screen.blit(
                    ship_sprite1, (16, game_settings.screen_height - 64 * 3.5))
                drawText(game_settings.screen, 'arial bold', "++ Damage",
                         22, 16 + 64 * 1.8, game_settings.screen_height - 64 * 3.35)
                drawText(game_settings.screen, 'arial bold', "-- Shields",
                         22, 16 + 64 * 1.85, game_settings.screen_height - 64 * 3.05)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        game_settings.ship = 1
                        select_sound.play()
                        waiting = False
            else:
                game_settings.screen.blit(
                    ship_sprite_locked, (16, game_settings.screen_height - 64 * 3.5))
                drawText(game_settings.screen, 'arial bold', "Reach a Highscore of 4269 to Unlock",
                         22, 16 + 64 * 3.3, game_settings.screen_height - 64 * 3.2)
            game_settings.screen.blit(ship_sprite2, (16, game_settings.screen_height - 98))
            ship2_rect = ship_sprite2.get_rect()
            ship2_rect.x = 16
            ship2_rect.y = game_settings.screen_height - 98

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    waiting = False
            pygame.display.flip()

        elif ship2_rect.collidepoint(pygame.mouse.get_pos()):
            draw_bg.DrawBackground(game_settings.screen, background_images,
                                   player, background_speed)
            drawText(game_settings.screen, 'comicsansms', "COOL",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2 - 100)
            drawText(game_settings.screen, 'comicsansms', "ASTEROID",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2)
            drawText(game_settings.screen, 'comicsansms', "GAME",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2 + 100)
            drawText(game_settings.screen, 'arial bold', "High Score: "
                     + str(game_settings.highscore), 24, game_settings.screen_width - 96, game_settings.screen_height - 32)
            game_settings.screen.blit(help_icon, (12, 12))
            if game_settings.highscore >= 4269:
                game_settings.screen.blit(
                    ship_sprite1, (16, game_settings.screen_height - 64 * 3.5))
            else:
                game_settings.screen.blit(
                    ship_sprite_locked, (16, game_settings.screen_height - 64 * 3.5))
            game_settings.screen.blit(ship_sprite2, (16, game_settings.screen_height - 98))

            drawText(game_settings.screen, 'arial bold', "++ Mag. Capacity",
                     22, 16 + 64 * 2.23, game_settings.screen_height - 64 * 1.35)
            drawText(game_settings.screen, 'arial bold', "++ Shields",
                     22, 16 + 64 * 1.85, game_settings.screen_height - 64 * 1.05)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    game_settings.ship = 2
                    game_settings.bullet_speed_factor = 45
                    game_settings.bullets_allowed = 10
                    game_settings.reload_time = 1770
                    game_settings.bullet_delay = 300
                    select_sound.play()
                    waiting = False
            pygame.display.flip()

        elif help_icon_rect.collidepoint(pygame.mouse.get_pos()):
            draw_bg.DrawBackground(game_settings.screen, background_images,
                                   player, background_speed)
            drawText(game_settings.screen, 'comicsansms', "COOL",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2 - 100)
            drawText(game_settings.screen, 'comicsansms', "ASTEROID",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2)
            drawText(game_settings.screen, 'comicsansms', "GAME",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2 + 100)
            drawText(game_settings.screen, 'arial bold', "High Score: "
                     + str(game_settings.highscore), 24, game_settings.screen_width - 96, game_settings.screen_height - 32)
            game_settings.screen.blit(help_icon, (12, 12))
            if game_settings.highscore >= 4269:
                game_settings.screen.blit(
                    ship_sprite1, (16, game_settings.screen_height - 64 * 3.5))
            else:
                game_settings.screen.blit(
                    ship_sprite_locked, (16, game_settings.screen_height - 64 * 3.5))
            game_settings.screen.blit(ship_sprite2, (16, game_settings.screen_height - 98))

            drawText(game_settings.screen, 'arial bold', "Move: WASD",
                     24, 146, 12 + 8)
            drawText(game_settings.screen, 'arial bold', " Shoot: SPACE",
                     24, 146, 12 * 2.5 + 8)
            drawText(game_settings.screen, 'arial bold', "Reload: R             ",
                     24, 146, 12 * 4 + 8)
            drawText(game_settings.screen, 'arial bold', "Complete each wave by shooting the asteroids down",
                     30, game_settings.screen_width / 2, 12 * 8 + 8)
            drawText(game_settings.screen, 'arial bold', "Collect powerups to boost your spaceship",
                     30, game_settings.screen_width / 2, 12 * 11 + 8)
            drawText(game_settings.screen, 'arial bold', "Select your spaceship here",
                     30, game_settings.screen_width / 2, game_settings.screen_height - 12 * 12)
            game_settings.screen.blit(bspeedup_sprite, (40 * 3.8, 190))
            game_settings.screen.blit(bspeeddown_sprite, (40 * 3.8, 190 + 76))
            game_settings.screen.blit(
                sspeedup_sprite, (game_settings.screen_width - 40 * 3.8 - 32, 190 + 28))
            game_settings.screen.blit(
                sspeeddown_sprite, (game_settings.screen_width - 40 * 3.8 - 32, 190 + 28 + 76))
            drawText(game_settings.screen, 'arial bold', "++ Fire Rate",
                     20, game_settings.screen_width / 2 - 57, 190)
            drawText(game_settings.screen, 'arial bold', "++ Movement Speed",
                     20, game_settings.screen_width / 2 + 28, 216)
            drawText(game_settings.screen, 'arial bold', "- - Fire Rate",
                     20, game_settings.screen_width / 2 - 57, 190 + 76)
            drawText(game_settings.screen, 'arial bold', "- - Movement Speed",
                     20, game_settings.screen_width / 2 + 28, 216 + 76)
            pygame.display.flip()

        else:
            draw_bg.DrawBackground(game_settings.screen, background_images,
                                   player, background_speed)
            drawText(game_settings.screen, 'comicsansms', "COOL",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2 - 100)
            drawText(game_settings.screen, 'comicsansms', "ASTEROID",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2)
            drawText(game_settings.screen, 'comicsansms', "GAME",
                     100, game_settings.screen_width / 2, game_settings.screen_height / 2 + 100)
            drawText(game_settings.screen, 'arial bold', "High Score: "
                     + str(game_settings.highscore), 24, game_settings.screen_width - 96, game_settings.screen_height - 32)
            game_settings.screen.blit(help_icon, (12, 12))
            if game_settings.highscore >= 4269:
                game_settings.screen.blit(
                    ship_sprite1, (16, game_settings.screen_height - 64 * 3.5))
            else:
                game_settings.screen.blit(
                    ship_sprite_locked, (16, game_settings.screen_height - 64 * 3.5))
            game_settings.screen.blit(ship_sprite2, (16, game_settings.screen_height - 98))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
