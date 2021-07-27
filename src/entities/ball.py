import random

import pygame
from src import constants as const
from src.entities.game_object import GameObject
from src.state.game_state import GameState


class Ball(GameObject):
    """
    A Ball GameObject
    """

    def __init__(self, game_state: GameState):
        """
        Initialize Ball class
        """
        super().__init__(game_state, game_state.assets.ball)
        self.rect.center = (const.WIDTH // 2, const.HEIGHT - 75)

        seed = random.choice([-1, 1]) * random.randint(1, 5)
        self.direction = pygame.Vector2(
            seed, random.randrange(2, 5) * abs(seed) * -1
        ).normalize()

    def update(self):
        """
        Run an update operation on the Ball object
        """
        if not self.game_state.in_play:
            self.rect.centerx = self.game_state["paddle"].rect.centerx
        else:
            if (
                self.rect.x + self.direction.x * const.BALL_SPEED < 0
                or self.rect.right + self.direction.x * const.BALL_SPEED > const.WIDTH
            ):
                self.direction.x *= -1
            if self.rect.y + self.direction.y * const.BALL_SPEED < 0:
                self.direction.y *= -1
            self.rect.center += self.direction * const.BALL_SPEED
