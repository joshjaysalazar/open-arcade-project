import pygame
import random
from src.player import Player
from src.enemies import Enemy
from src.core import constants


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        # Set up sprite groups
        self.player_sprites = pygame.sprite.Group()
        self.player_bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_bullet_sprites = pygame.sprite.Group()

        self.create_level()

    def create_level(self):
        self.player = Player(
            1,
            (50, 50),
            [self.player_sprites],
            self.player_bullet_sprites
            )

    def spawn_enemies(self):
        # NOTE: This is a temporary solution to get enemies on screen
        spawn_chance = random.randint(1, 50)
        if spawn_chance == 1:
            x_pos = random.randint(0, constants.SCREEN_WIDTH - 20)
            Enemy(
                (x_pos, -20),
                [self.enemy_sprites],
                self.enemy_bullet_sprites,
                self.player_bullet_sprites
                )

    def run(self):
        self.spawn_enemies()

        self.enemy_sprites.update()
        self.enemy_sprites.draw(self.display_surface)

        self.enemy_bullet_sprites.update()
        self.enemy_bullet_sprites.draw(self.display_surface)

        self.player_sprites.update()
        self.player_sprites.draw(self.display_surface)

        self.player_bullet_sprites.update()
        self.player_bullet_sprites.draw(self.display_surface)
