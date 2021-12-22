import pygame
rel_x, par_y1 = 0, -1024
par_y2 = 0
par_y3 = 0
vec = pygame.math.Vector2


def DrawBackground(screen, background_images, player, speed):
    global par_y1, par_y2, par_y3
    global rel_x

    background = background_images[0]
    par1 = background_images[1]
    par2 = background_images[2]
    par3 = background_images[3]
    bg_rect = background_images[4]
    screen_rect = screen.get_rect()

    keys = pygame.key.get_pressed()

    rel_par_y1 = -bg_rect.h + screen_rect.h + par_y1 % bg_rect.h
    rel_par_y2 = -bg_rect.h + screen_rect.h + par_y2 % bg_rect.h
    rel_par_y3 = -bg_rect.h + screen_rect.h + par_y3 % bg_rect.h

    screen.blit(background, (-(bg_rect.w - screen_rect.w) / 2 + rel_x, 0))
    if rel_par_y1 >= 0:
        screen.blit(par1, (-(bg_rect.w - screen_rect.w) / 2 + rel_x, rel_par_y1 - bg_rect.h))
        screen.blit(par2, (-(bg_rect.w - screen_rect.w) / 2 + rel_x, rel_par_y2 - bg_rect.h))
        screen.blit(par3, (-(bg_rect.w - screen_rect.w) / 2 + rel_x, rel_par_y3 - bg_rect.h))

    if (-(bg_rect.w - screen_rect.w) / 2 + rel_x < 0)\
       and player.rect.centerx < screen_rect.w / 2:
        rel_x += 0.25
    if (-(bg_rect.w - screen_rect.w) / 2 + rel_x > -(bg_rect.w - screen_rect.w))\
            and player.rect.centerx > screen_rect.w / 2:
        rel_x -= 0.25

    if player.alive is True:
        if keys[pygame.K_LEFT] and keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            if (-(bg_rect.w - screen_rect.w) / 2 + rel_x < 0) and not keys[pygame.K_RIGHT]\
               and player.rect.centerx < screen_rect.w / 2:
                rel_x += 0.10

        elif keys[pygame.K_RIGHT] and keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            if (-(bg_rect.w - screen_rect.w) / 2 + rel_x > -(bg_rect.w - screen_rect.w)) and not keys[pygame.K_LEFT]\
                    and player.rect.centerx > screen_rect.w / 2:
                rel_x -= 0.10

        elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
            par_y1 += 1.5 / 3 * speed
            par_y2 += 4 / 6 * speed
            par_y3 += 6 / 6 * speed
            if (-(bg_rect.w - screen_rect.w) / 2 + rel_x < 0) and not keys[pygame.K_RIGHT]\
               and player.rect.centerx < screen_rect.w / 2:
                rel_x += 0.10

        elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
            par_y1 += 1.5 / 3 * speed
            par_y2 += 4 / 6 * speed
            par_y3 += 6 / 6 * speed
            if (-(bg_rect.w - screen_rect.w) / 2 + rel_x) > -(bg_rect.w - screen_rect.w) and not keys[pygame.K_LEFT]\
               and player.rect.centerx > screen_rect.w / 2:
                rel_x -= 0.10

        elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
            if (-(bg_rect.w - screen_rect.w) / 2 + rel_x) > -(bg_rect.w - screen_rect.w) and not keys[pygame.K_LEFT]\
               and player.rect.centerx > screen_rect.w / 2:
                rel_x -= 0.10

        elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
            if (-(bg_rect.w - screen_rect.w) / 2 + rel_x < 0) and not keys[pygame.K_RIGHT]\
               and player.rect.centerx < screen_rect.w / 2:
                rel_x += 0.10

        elif keys[pygame.K_LEFT]:
            if (-(bg_rect.w - screen_rect.w) / 2 + rel_x < 0) and not keys[pygame.K_RIGHT]\
               and player.rect.centerx < screen_rect.w / 2:
                rel_x += 0.10

        elif keys[pygame.K_RIGHT]:
            if (-(bg_rect.w - screen_rect.w) / 2 + rel_x > -(bg_rect.w - screen_rect.w)) and not keys[pygame.K_LEFT]\
               and player.rect.centerx > screen_rect.w / 2:
                rel_x -= 0.10

        elif keys[pygame.K_UP]:
            par_y1 += 1.5 / 4 * speed
            par_y2 += 4 / 6 * speed
            par_y3 += 6 / 6 * speed

    par_y1 += 1 * speed
    par_y2 += 2 * speed
    par_y3 += 4 * speed

    screen.blit(par1, (-(bg_rect.w - screen_rect.w) / 2 + rel_x, rel_par_y1))
    screen.blit(par2, (-(bg_rect.w - screen_rect.w) / 2 + rel_x, rel_par_y2))
    screen.blit(par3, (-(bg_rect.w - screen_rect.w) / 2 + rel_x, rel_par_y3))
