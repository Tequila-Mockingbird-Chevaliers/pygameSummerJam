import pygame

from src.entities.ball import Ball
from src.entities.paddle import Paddle
from src.scenes.scene import Scene


class GameScene(Scene):
    def __init__(self, program):
        super().__init__(program)
        self.in_play = False
        self.paddle = self.object_manager.add_object("paddle", Paddle(self))
        self.ball = self.object_manager.add_object("ball", Ball(self))

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
        self.object_manager.update()

    def render(self, screen: pygame.Surface):
        screen.fill("LIGHTGRAY")
        self.object_manager.render(screen)

    def ball_paddle_collision(self):
        self.ball.direction.y *= -1
