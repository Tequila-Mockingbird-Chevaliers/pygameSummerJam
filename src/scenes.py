from typing import Optional
from abc import ABC, abstractmethod
import pygame
from main import SpaceBreaker
import object_manager
import game_objects


class Scene(ABC):
    def __init__(self, program):
        self.program = program
        self.object_manager: object_manager.ObjectManager = object_manager.ObjectManager(self.program)

    def start(self):
        pass

    @abstractmethod
    def events(self, events):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    def end(self):
        self.object_manager.clear_objects()


class SceneManager:
    def __init__(self, program):
        self.scene: Optional[Scene] = None
        self.program: SpaceBreaker = program

    def go_to(self, scene: Scene):
        if self.scene:
            self.scene.end()
        self.scene = scene
        self.scene.start()


class GameScene(Scene):
    def __init__(self, program):
        super().__init__(program)
        self.in_play = False
        self.paddle = self.object_manager.add_object('paddle', game_objects.Paddle(self))
        self.ball = self.object_manager.add_object('ball', game_objects.Ball(self))

    def events(self, events):
        self.object_manager.events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.in_play = True

    def update(self):
        if self.in_play:
            self.object_manager.test_collision('ball', 'paddle', self.ball_paddle_collision)
        self.object_manager.update()

    def render(self, screen: pygame.Surface):
        screen.fill("LIGHTGRAY")
        self.object_manager.render(screen)

    def ball_paddle_collision(self):
        self.ball.direction.y *= -1
