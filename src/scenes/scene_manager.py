from typing import Optional

from src.scenes.scene import Scene


class SceneManager:
    """
    SceneManager class
    """

    def __init__(self):
        """
        Initialise SceneManager class
        """
        self.scene: Optional[Scene] = None

    def go_to(self, scene: Scene):
        """
        Change the scene
        """
        if self.scene is not None:
            self.scene.end()

        self.scene = scene
        self.scene.start()
