import random
from src.entities.game_object import GameObject
import src.constants as const


class Brick(GameObject):
    def __init__(self, game, grid_x, grid_y):
        image = game.program.assets.images[f'BRICK{random.randint(0, const.NO_OF_BRICK_IMAGES - 1)}']
        rect = image.get_rect()
        rect.topleft = (grid_x * 50, 300 + grid_y * 20)
        super().__init__(game, image, rect)

    def remove(self):
        self.game.add_score(10)
