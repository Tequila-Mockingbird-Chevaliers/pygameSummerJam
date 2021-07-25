import pygame

from src import constants as const
from src.entities.game_object import GameObject


class Paddle(GameObject):
    def __init__(self, game):
        image = game.program.assets.images['PADDLE']
        rect = image.get_rect()
        rect.center = (const.WIDTH // 2, const.HEIGHT - 50)
        super().__init__(game, image, rect)
        self.direction = 0

    def events(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if (
                    event.key == pygame.K_LEFT
                    and self.direction == -1
                    or event.key == pygame.K_RIGHT
                    and self.direction == 1
                ):
                    self.direction = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = -1
                if event.key == pygame.K_RIGHT:
                    self.direction = 1

    def update(self):
        if self.direction:
            self.rect.x += const.PADDLE_SPEED * self.direction
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.right > const.WIDTH:
                self.rect.right = const.WIDTH
