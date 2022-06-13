import pygame

# Init font
pygame.font.init()
font = pygame.font.Font(None, 24)


def output(info, x=10, y=10):
    # Get the main display surface
    display_surface = pygame.display.get_surface()

    # Prepare the debug output
    surf = font.render(str(info), True, "white")
    rect = surf.get_rect(topleft=(x, y))

    # Draw the debug output
    pygame.draw.rect(display_surface, "black", rect)
    display_surface.blit(surf, rect)
