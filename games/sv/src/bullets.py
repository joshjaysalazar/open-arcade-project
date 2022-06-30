import pygame
from src.core import constants


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, owner, pos, groups):
        super().__init__(groups)

        # Expose owner to class
        self.owner = owner

        # Create image and rect
        # Load both images
        self.image = pygame.image.load(
            "res/img/player/bullet.png"
            ).convert_alpha()
        self.image.fill(constants.RED, special_flags=pygame.BLEND_MULT)
        self.rect = self.image.get_rect(midbottom=pos)

        # Movement variables
        self.direction = pygame.math.Vector2()
        self.direction.y = -1
        self.speed = 5

    def move(self):
        self.rect.center += self.direction * self.speed

    def check_off_screen(self):
        if self.rect.bottom <= 0:
            self.kill()

    def update(self):
        self.move()
        self.check_off_screen()
