import pygame

from src.core import constants


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, enemy_bullets, player_bullets):
        super().__init__(groups)

        # Expose sprite groups to class
        self.enemy_bullets = enemy_bullets
        self.player_bullets = player_bullets

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

    def check_collisions(self):
        other_sprite = pygame.sprite.spritecollideany(
            self,
            self.player_bullets
            )
        if other_sprite is not None:
            other_sprite.kill()
            self.kill()

    def update(self):
        # Tick down the cooldown counter
        if self.cooldown_counter > 0:
            self.cooldown_counter -= 1
        else:
            self.cooldown_counter = 0

        self.move()
        self.check_collisions()
