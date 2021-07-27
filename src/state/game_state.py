import pygame

from src.entities.object_manager import ObjectManager
from src.assets import Assets


class GameState(ObjectManager):
    """
    Represent the state of the game
    """

    def __init__(self):
        """
        Initialize gamestate class
        """
        super().__init__()
        self.assets = Assets()
        self.score: int = 0
        self.in_play: bool = False
        self.defeat: bool = False
        self.victory: bool = False

    def add_score(self, amount: int):
        """
        Update player score
        """
        self.score += amount

    def render(self, screen: pygame.Surface):
        """
        Render GameState
        """
        super().render(screen)
        if self.defeat:
            screen.blit(self.assets.defeat_text, (screen.get_width() // 2 - self.assets.defeat_text.get_width() // 2,
                                                  screen.get_height() // 2 - self.assets.defeat_text.get_height() // 2))
