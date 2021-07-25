from typing import Optional

from main import SpaceBreaker
from src.scenes.scene import Scene


class SceneManager:
    def __init__(self, program):
        self.scene: Optional[Scene] = None
        self.program: SpaceBreaker = program

    def go_to(self, scene: Scene):
        if self.scene:
            self.scene.end()
        self.scene = scene
        self.scene.start()
