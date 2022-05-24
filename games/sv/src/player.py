import pygame
from src.core import constants


class Player(pygame.sprite.Sprite):
    def __init__(self, player_number, pos, groups, bullet_group):
        super().__init__(groups)

        # Expose sprite groups to class
        self.bullet_group = bullet_group

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

        # Set up variables
        self.direction = pygame.math.Vector2()
        self.speed = 4
        self.cooldown_time = 15
        self.cooldown_counter = 0

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

        if keys[pygame.K_SPACE]:
            self.fire()

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

            self.rect.center += self.direction * self.speed

    def fire(self):
        if self.cooldown_counter <= 0:
            PlayerBullet(self, self.rect.midtop, [self.bullet_group])

            # Set cooldown counter
            self.cooldown_counter = self.cooldown_time

    def update(self):
        # Tick down the cooldown counter
        if self.cooldown_counter > 0:
            self.cooldown_counter -= 1
        else:
            self.cooldown_counter = 0

        self.input()
        self.move()


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
