from src.entities.object_manager import ObjectManager
from src.assets import Assets


class GameState(ObjectManager):
    """
    Represent the state of the game
    """

    def __init__(self):
        """
        Initialise gamestate class
        """
        super().__init__()
        self.assets = Assets()
        self.score: int = 0
        self.in_play: bool = False

    def add_score(self, amount: int):
        """
        Update player score
        """
        self.score += amount
