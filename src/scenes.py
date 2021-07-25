from typing import Optional
from abc import ABC, abstractmethod
from main import SpaceBreaker


class Scene(ABC):
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
        pass


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
    def events(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        pass
