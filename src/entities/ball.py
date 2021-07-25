import random

import pygame

from src import constants as const
from src.entities.game_object import GameObject


class Ball(GameObject):
    def __init__(self, game):
        image = game.program.assets.images['BALL']
        rect = image.get_rect()
        rect.center = (const.WIDTH // 2, const.HEIGHT - 75)
        super().__init__(game, image, rect)
        seed = random.choice([-1, 1]) * random.randint(1, 5)
        self.direction = pygame.Vector2(
            seed, random.randrange(2, 5) * abs(seed) * -1
        ).normalize()

    def update(self):
        if not self.game.in_play:
            self.rect.centerx = self.game.paddle.rect.centerx
        else:
            if (
                self.rect.x + self.direction.x * const.BALL_SPEED < 0
                or self.rect.right + self.direction.x * const.BALL_SPEED > const.WIDTH
            ):
                self.direction.x *= -1
            if self.rect.y + self.direction.y * const.BALL_SPEED < 0:
                self.direction.y *= -1
            self.rect.center += self.direction * const.BALL_SPEED
