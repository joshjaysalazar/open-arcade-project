import pygame
from src.player import Player


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.player_sprites = pygame.sprite.Group()
        self.create_level()

    def create_level(self):
        self.player = Player(1, (50, 50), [self.player_sprites])

    def run(self):
        self.player_sprites.draw(self.display_surface)
        self.player_sprites.update()
