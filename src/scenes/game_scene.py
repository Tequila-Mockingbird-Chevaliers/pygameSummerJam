from __future__ import annotations

import random
from collections import Set

import pygame
import src.constants as const
from src.entities.ball import Ball
from src.entities.brick import Brick
from src.entities.brick_generator import BrickGenerator
from src.entities.object_manager import ObjectGroup
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
        Initialize GameScene object
        """
        super().__init__(game_state)
        self.spaceship_spawn_timer = None
        self.free_positions = set()
        self.initialize_game()

    def initialize_game(self):
        self.current_level = 1
        self.game_state.score = 0
        self.game_state.game_finished = False
        self.initialize_level()

    def initialize_level(self):
        self.game_state.init_game()
        self.game_state.clear_objects()
        self.game_state.add_object("paddle", Paddle(self.game_state))
        self.game_state.add_object("ball", Ball(self.game_state))
        self.game_state.create_object_group("spaceships")
        self.spaceship_spawn_timer = Timer(const.SPACESHIP_SPAWN_TIMER)
        self.free_positions = {0, 1, 2, 3, 4, 5}
        brick_generator = BrickGenerator(self.current_level)
        for brick_pos in brick_generator.bricks:
            self.game_state.add_object("bricks", Brick(self.game_state, brick_pos))

    def initialize_new_play(self):
        self.game_state.in_play = False
        self.game_state.remove_object(self.game_state["paddle"])
        self.game_state.add_object("paddle", Paddle(self.game_state))
        self.game_state.remove_object(self.game_state["ball"])
        self.game_state.add_object("ball", Ball(self.game_state))

    def events(self, events: list[pygame.event.Event]):
        """
        Handle events
        """
        self.game_state.events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not self.game_state.in_play:
                    self.game_state.start()

                elif event.key == pygame.K_r:
                    self.initialize_game()

                elif event.key in [
                    pygame.K_SPACE,
                    pygame.K_RETURN,
                ]:
                    if self.game_state.defeat:
                        self.initialize_game()
                    elif self.game_state.victory and not self.game_state.game_finished:
                        self.initialize_level()

    def update(self):
        """
        Update game logic
        """
        if not self.game_state.defeat and not self.game_state.victory:
            if self.game_state.in_play:
                self.check_end_conditions()
                self.game_state.test_collision(
                    "ball", "paddle", self.ball_paddle_collision
                )
                self.game_state.test_collision(
                    "ball", "bricks", self.ball_brick_collision
                )
                self.game_state.test_collision(
                    "ball", "spaceships", self.ball_spaceship_collision
                )
                if (
                        self.spaceship_spawn_timer.check_time()
                        and len(self.free_positions) > 1
                ):
                    position = random.choice(tuple(self.free_positions))
                    self.free_positions.remove(position)
                    self.game_state.add_object(
                        "spaceships", Spaceship(self.game_state, position)
                    )

        if self.game_state.update():
            self.initialize_level()

    def render(self, screen: pygame.Surface):
        """
        Render game window
        """
        screen.blit(self.game_state.assets.bg_images[0], (0, 0))
        self.game_state.render(screen)

    def ball_paddle_collision(self, objects):
        """
        Handle ball and paddle collision
        """
        self.game_state.assets.paddle_sound.play()
        ball = self.game_state["ball"]
        paddle = self.game_state["paddle"]
        ball.direction.y *= -1
        angle = (1 - (ball.rect.centerx - paddle.rect.x) / paddle.rect.width) * 120 + 30
        direction = pygame.math.Vector2(1, 0).rotate(angle)
        direction.y *= -1
        ball.direction = direction

    def ball_brick_collision(self, objects):
        """
        Handle ball-brick collision
        """
        self.game_state.assets.block_sound.play()
        ball = self.game_state["ball"]
        ball.direction.y *= -1
        self.game_state.remove_object(objects[1])

    def ball_spaceship_collision(self, objects):
        """
        Handle ball-spaceship collision
        """
        self.game_state.assets.tingle_sound.play()
        ball = self.game_state["ball"]
        ball.direction.y *= -1
        self.free_positions.add(objects[1].line)
        self.game_state.remove_object(objects[1])

    def check_end_conditions(self):
        ball = self.game_state["ball"]
        paddle = self.game_state["paddle"]
        lasers = (
            self.game_state.objects["lasers"]
            if "lasers" in self.game_state.objects
            else ObjectGroup()
        )
        # Check defeat conditions
        if ball.rect.y > const.HEIGHT:
            self.handle_defeat()
            return

        for laser in lasers:
            if laser.rect.colliderect(paddle.rect):
                self.handle_defeat()
                return

        # Check victory conditions
        bricks = self.game_state.objects["bricks"].objects
        if not bricks:
            self.handle_victory()
            return

    def handle_defeat(self):
        self.game_state.lives -= 1
        if self.game_state.lives <= 0:
            self.game_state.defeat = True
        else:
            self.game_state.score -= 50
            self.initialize_new_play()

    def handle_victory(self):
        self.game_state.victory = True
        self.current_level += 1
        if self.current_level > const.MAX_LEVEL:
            self.game_state.game_finished = True
        else:
            self.game_state.timer_before_next_level.start_timer()
