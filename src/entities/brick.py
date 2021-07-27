from __future__ import annotations

import random

from src.constants import BRICK_WIDTH, BRICK_HEIGHT
from src.entities.game_object import GameObject
from src.state.game_state import GameState


class Brick(GameObject):
    """
    Brick object
    """

    def __init__(self, game_state: GameState, grid: tuple[int, int]):
        """
        Initialize Brick class
        """
        super().__init__(game_state, random.choice(game_state.assets.bricks))
        self.rect.topleft = (grid[0] * BRICK_WIDTH, 300 + grid[1] * BRICK_HEIGHT)

    def remove(self):
        """
        When the brick is removed, increment score
        """
        self.game_state.add_score(10)
