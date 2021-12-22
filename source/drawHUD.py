import pygame


def drawHUD(screen, x, y, percent_shields, percent_health, images, ship):
    if percent_shields < 0:
        percent_shields = 0
    if percent_health < 0:
        percent_health = 0

    bullet_sprite = images.bullet_frames[0]
    screen_rect = screen.get_rect()
    bar_length = 150
    bar_height = 13
    fill_shields = percent_shields / 100 * bar_length
    fill_health = percent_health / 100 * bar_length

    if ship == 1:
        outline_shields_rect = pygame.Rect(x, y, bar_length / 4, bar_height)
    if ship == 2:
        outline_shields_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_shields_rect = pygame.Rect(x, y, fill_shields, bar_height)
    outline_health_rect = pygame.Rect(x, y + bar_height + 7, bar_length, bar_height)
    fill_health_rect = pygame.Rect(x, y + bar_height + 7, fill_health, bar_height)
    pygame.draw.rect(screen, (0, 134, 211), fill_shields_rect)
    pygame.draw.rect(screen, (255, 255, 255), outline_shields_rect, 1)
    pygame.draw.rect(screen, (255, 61, 35), fill_health_rect)
    pygame.draw.rect(screen, (255, 255, 255), outline_health_rect, 1)
    if ship == 1:
        screen.blit(bullet_sprite, (screen_rect.width - 81, screen_rect.height - 38))
    if ship == 2:
        screen.blit(bullet_sprite, (screen_rect.width - 69, screen_rect.height - 32))
