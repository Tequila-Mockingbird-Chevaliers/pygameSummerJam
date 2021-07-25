import pygame

from src.entities.game_object import GameObject


class Brick(GameObject):
    def __init__(self, game, grid_x, grid_y):
        image = pygame.Surface((50, 20))
        image.fill("BLUE")
        rect = image.get_rect()
        rect.topleft = (grid_x * 50, 300 + grid_y * 20)
        super().__init__(game, image, rect)

    def remove(self):
        self.game.add_score(10)
        print(self.game.score)
