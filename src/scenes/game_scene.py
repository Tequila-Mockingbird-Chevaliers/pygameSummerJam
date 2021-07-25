import pygame

from src.entities.ball import Ball
from src.entities.paddle import Paddle
from src.entities.brick_generator import BrickGenerator
from src.entities.brick import Brick
from src.scenes.scene import Scene


class GameScene(Scene):
    def __init__(self, program):
        super().__init__(program)
        self.in_play = False
        self.paddle = self.object_manager.add_object("paddle", Paddle(self))
        self.ball = self.object_manager.add_object("ball", Ball(self))
        brick_generator = BrickGenerator("1")
        for brick_pos in brick_generator.bricks:
            self.object_manager.add_object(
                "bricks", Brick(self, brick_pos[1], brick_pos[0])
            )

    def events(self, events):
        self.object_manager.events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.in_play = True

    def update(self):
        if self.in_play:
            self.object_manager.test_collision(
                "ball", "paddle", self.ball_paddle_collision
            )
            self.object_manager.test_collision('ball', 'bricks', self.ball_brick_collision)
        self.object_manager.update()

    def render(self, screen: pygame.Surface):
        screen.fill("LIGHTGRAY")
        self.object_manager.render(screen)

    def ball_paddle_collision(self, objects):
        self.ball.direction.y *= -1
        angle = (
            1 - (self.ball.rect.centerx - self.paddle.rect.x) / self.paddle.rect.width
        ) * 120 + 30
        direction = pygame.math.Vector2(1, 0).rotate(angle)
        direction.y *= -1
        self.ball.direction = direction

    def ball_brick_collision(self, objects):
        self.object_manager.remove_object(objects[1])
