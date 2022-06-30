import pygame
from src.core import constants

# Init font
pygame.font.init()
font = pygame.font.Font("res/fonts/PressStart2P-Regular.ttf", 8)


def output(info, x=10, y=10):
    # Get the main display surface
    display_surface = pygame.display.get_surface()

    # Prepare the debug output
    surf = font.render(str(info), False, constants.WHITE)
    rect = surf.get_rect(topleft=(x, y))

    # Draw the debug output
    pygame.draw.rect(display_surface, constants.BLACK, rect)
    display_surface.blit(surf, rect)
