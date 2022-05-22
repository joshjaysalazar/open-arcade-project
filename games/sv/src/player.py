import pygame
from src.core import constants


class Player(pygame.sprite.Sprite):
    def __init__(self, player_number, pos, groups):
        super().__init__(groups)

        # Load both images
        primary = pygame.image.load(
            "res/img/player/primary.png"
            ).convert_alpha()
        secondary = pygame.image.load(
            "res/img/player/secondary.png"
            ).convert_alpha()
        primary.fill(constants.RED, special_flags=pygame.BLEND_MULT)
        secondary.fill(constants.BLUE, special_flags=pygame.BLEND_MULT)
        self.image = primary
        self.image.blit(secondary, (0, 0))
        self.rect = self.image.get_rect(topleft=pos)

        # Set up movement variables
        self.direction = pygame.math.Vector2()
        self.speed = 5

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            self.rect.center += self.direction * speed

    def update(self):
        self.input()
        self.move(self.speed)
