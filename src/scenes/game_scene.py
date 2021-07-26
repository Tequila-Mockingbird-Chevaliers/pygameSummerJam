from __future__ import annotations

import random

import pygame
import src.constants as const
from src.entities.ball import Ball
from src.entities.brick import Brick
from src.entities.brick_generator import BrickGenerator
from src.entities.paddle import Paddle
from src.entities.spaceship import Spaceship
from src.scenes.scene import Scene
from src.state.game_state import GameState
from src.timer import Timer


class GameScene(Scene):
    """
    GameScene object
    """

    def __init__(self, game_state: GameState):
        """
        Initialise GameScene object
        """
        super().__init__(game_state)

        self.game_state.add_object("paddle", Paddle(game_state))
        self.game_state.add_object("ball", Ball(game_state))
        self.spaceship_spawn_timer = Timer(const.SPACESHIP_SPAWN_TIMER)
        self.free_positions = [0, 1, 2, 3, 4, 5]
        brick_generator = BrickGenerator(1)
        for brick_pos in brick_generator.bricks:
            self.game_state.add_object("bricks", Brick(game_state, brick_pos))

    def events(self, events: list[pygame.event.Event]):
        self.game_state.events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game_state.in_play = True

    def update(self):
        if self.game_state.in_play:
            self.game_state.test_collision("ball", "paddle", self.ball_paddle_collision)
            self.game_state.test_collision("ball", "bricks", self.ball_brick_collision)
            if self.spaceship_spawn_timer.check_time() and len(self.free_positions) > 1:
                position = random.choice(self.free_positions)
                self.free_positions.remove(position)
                self.game_state.add_object(
                    "spacehips", Spaceship(self.game_state, position)
                )

        self.game_state.update()

    def render(self, screen: pygame.Surface):
        screen.fill("LIGHTGRAY")
        self.game_state.render(screen)

    def ball_paddle_collision(self, objects):
        ball = self.game_state["ball"]
        paddle = self.game_state["paddle"]
        ball.direction.y *= -1
        angle = (1 - (ball.rect.centerx - paddle.rect.x) / paddle.rect.width) * 120 + 30
        direction = pygame.math.Vector2(1, 0).rotate(angle)
        direction.y *= -1
        ball.direction = direction

    def ball_brick_collision(self, objects):
        self.game_state.remove_object(objects[1])
