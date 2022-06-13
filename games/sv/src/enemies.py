import pygame

from src import bullets
from src.core import constants


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, bullet_group):
        super().__init__(groups)

        # Expose sprite groups to class
        self.bullet_group = bullet_group

        # Load the enemy image
        self.image = pygame.image.load(
            "res/img/enemies/enemy.png"
            ).convert_alpha()
        self.image.fill(constants.RED, special_flags=pygame.BLEND_MULT)
        self.rect = self.image.get_rect(topleft=pos)

        # Set up variables
        self.direction = pygame.math.Vector2()
        self.direction.y = 1
        self.speed = 2
        self.cooldown_time = 15
        self.cooldown_counter = 0

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            self.rect.center += self.direction * self.speed

    # def fire(self):
    #     if self.cooldown_counter <= 0:
    #         bullets.PlayerBullet(self, self.rect.midtop, [self.bullet_group])
    #
    #         # Set cooldown counter
    #         self.cooldown_counter = self.cooldown_time

    def update(self):
        # Tick down the cooldown counter
        if self.cooldown_counter > 0:
            self.cooldown_counter -= 1
        else:
            self.cooldown_counter = 0

        self.move()
