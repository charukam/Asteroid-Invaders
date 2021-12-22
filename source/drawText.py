import pygame


def drawText(screen, font, text, size, x, y):
    font_name = pygame.font.match_font(font)
    font = pygame.font.SysFont(font_name, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)
