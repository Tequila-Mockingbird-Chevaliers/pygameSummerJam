import random

from src.entities.game_object import GameObject
from src.state.game_state import GameState


class Brick(GameObject):
    def __init__(self, game_state: GameState, grid):
        self.image = random.choice(game_state.assets.bricks)
        self.rect = self.image.get_rect()
        self.rect.topleft = (grid[0] * 50, 300 + grid[1] * 20)
        self.game_state = game_state

    def remove(self):
        self.game_state.add_score(10)
