import random

from src.entities.game_object import GameObject
from src.state.game_state import GameState


class Brick(GameObject):
    def __init__(self, game_state: GameState, grid):
        super().__init__(game_state, random.choice(game_state.assets.bricks))
        self.rect.topleft = (grid[0] * 50, 300 + grid[1] * 20)

    def remove(self):
        self.game_state.add_score(10)
