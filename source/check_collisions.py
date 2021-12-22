import pygame
from explosion import Explosion
from powerup import Powerup
from random import choice
from random import choices
from random import randint
from random import random
from asteroid import Asteroid

dead_flag = True
timer_flag = False
delay_time = 0


def check_collisions(sprite_group, explode_sounds, images, game_settings, player, ship_explode_sound, powerup_sound, wall_sprite, rand_val):
    now = pygame.time.get_ticks()

    # Check collisions on mobs
    close_hits = pygame.sprite.groupcollide(sprite_group.mobs, sprite_group.bullets, False, False)
    if close_hits:
        if game_settings.ship == 1:
            mask_hits = pygame.sprite.groupcollide(
                sprite_group.mobs, sprite_group.bullets, True, False, pygame.sprite.collide_mask)
        if game_settings.ship == 2:
            mask_hits = pygame.sprite.groupcollide(
                sprite_group.mobs, sprite_group.bullets, True, True, pygame.sprite.collide_mask)

        for hit in mask_hits:
            choice(explode_sounds).play()
            rand_val = choices([0, 1, 2])
            if hit.rect.width <= 47:
                explode = Explosion(images, hit.rect.center, 'small')
                game_settings.score += 100
            elif hit.rect.width <= 75:
                explode = Explosion(images, hit.rect.center, 'med')
                game_settings.score += 50
            else:
                explode = Explosion(images, hit.rect.center, 'large')
                game_settings.score += 25
            sprite_group.all_sprites.add(explode)
            powerup_chance = random()
            if powerup_chance > 1 - game_settings.powerup_frequency:
                powerup_type = choice(['bullet_speed_up', 'bullet_speed_down',
                                       'ship_speed_up', 'ship_speed_down'])
                powerup = Powerup(images, hit.rect.center, powerup_type)
                sprite_group.all_sprites.add(powerup)
                sprite_group.powerups.add(powerup)

    # Check collisions on player
    close_hits = pygame.sprite.spritecollide(player, sprite_group.mobs, False)
    if close_hits:
        mask_hits = pygame.sprite.spritecollide(
            player, sprite_group.mobs, True, pygame.sprite.collide_mask)
        for hit in mask_hits:
            ship_explode_sound.play()
            rand_val = choices([0, 1, 2])
            if hit.rect.width <= 47:
                game_settings.score -= 50
                if player.shield > 0:
                    player.shield -= 16
                    explode = Explosion(images, hit.rect.center, 'tiny')
                    if player.shield < 0:
                        player.health += player.shield * 34 / 16
                        explode = Explosion(images, hit.rect.center, 'small')
                else:
                    player.health -= 34
                    explode = Explosion(images, hit.rect.center, 'small')

            elif hit.rect.width <= 75:
                game_settings.score -= 100
                if player.shield > 0:
                    player.shield -= 33
                    explode = Explosion(images, hit.rect.center, 'med')
                    if player.shield < 0:
                        player.health += player.shield * 50 / 33
                        explode = Explosion(images, hit.rect.center, 'large')
                else:
                    player.health -= 50
                    explode = Explosion(images, hit.rect.center, 'large')

            else:
                game_settings.score -= 250
                if player.shield > 0:
                    player.shield -= 47
                    explode = Explosion(images, hit.rect.center, 'large')
                    if player.shield < 0:
                        player.health += player.shield * 75 / 47
                        explode = Explosion(images, hit.rect.center, 'huge')
                else:
                    player.health -= 75
                    explode = Explosion(images, hit.rect.center, 'huge')

            asteroid = Asteroid(game_settings, rand_val, images)
            sprite_group.mobs.add(asteroid)
            sprite_group.all_sprites.add(asteroid)
            sprite_group.all_sprites.add(explode)

            if player.health <= 0:
                explode = Explosion(images, hit.rect.center, 'massive')
                for i in range(20):
                    rand_cord_x = randint(-164, 164)
                    rand_cord_y = randint(-164, 164)
                    explode_med = Explosion(
                        images, (hit.rect.centerx + rand_cord_x, hit.rect.centery + rand_cord_y), 'med')
                    sprite_group.all_sprites.add(explode_med)
                for i in range(10):
                    rand_cord_x = randint(-164, 164)
                    rand_cord_y = randint(-164, 164)
                    explode_large = Explosion(
                        images, (hit.rect.centerx + rand_cord_x, hit.rect.centery + rand_cord_y), 'huge')
                    sprite_group.all_sprites.add(explode_large)
                sprite_group.all_sprites.add(explode)
                player.alive = False
                player.pos.x = 9000

    if player.alive is False:
        game_settings.dead_flag = False
        if game_settings.dead_flag is False:
            if game_settings.timer_flag is False:
                game_settings.delay_time2 = now
                game_settings.timer_flag = True
            if now - game_settings.delay_time2 > 4000:
                game_settings.delay_time2 = now + 4000
                game_settings.game_over = True

    # Check collisions with wall
    hits = pygame.sprite.spritecollide(wall_sprite, sprite_group.mobs, True)
    for hit in hits:
        if hit.rect.width <= 47:
            game_settings.score -= 7
        elif hit.rect.width <= 75:
            game_settings.score -= 18
        else:
            game_settings.score -= 78

        asteroid = Asteroid(game_settings, rand_val, images)
        sprite_group.mobs.add(asteroid)
        sprite_group.all_sprites.add(asteroid)

    # Check collisions on powerups
    close_hits = pygame.sprite.spritecollide(player, sprite_group.powerups, False)
    if close_hits:
        mask_hits = pygame.sprite.spritecollide(
            player, sprite_group.powerups, True, pygame.sprite.collide_mask)
        for hit in mask_hits:
            powerup_sound.play()
            if hit.type == 'bullet_speed_up':
                game_settings.bullet_delay -= 10
            if hit.type == 'bullet_speed_down':
                game_settings.bullet_delay += 10
                if game_settings.bullet_delay < 50:
                    game_settings.bullet_delay = 50
            if hit.type == 'ship_speed_up':
                game_settings.ship_acc += 0.03
                if game_settings.ship_acc > 3:
                    game_settings.ship_acc = 3
            if hit.type == 'ship_speed_down':
                game_settings.ship_acc -= 0.03
                if game_settings.ship_acc < 0.08:
                    game_settings.ship_acc = 0.08

    if player.shield <= 0 and player.shield >= -1000:
        explode = Explosion(images, player.rect.center, 'shield')
        sprite_group.all_sprites.add(explode)
        player.shield = -2000
