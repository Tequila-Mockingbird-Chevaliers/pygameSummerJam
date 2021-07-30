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
        self.victory_sound_played = False

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
        score_text = self.assets.score_font.render(
            f"SCORE : {self.score}", True, pygame.Color("black")
        )
        screen.blit(score_text, (0, self.assets.score_font.get_height() // 2))
        if self.defeat:
            GameState.__blit_text_at_center(screen, self.assets.defeat_text)

        elif self.victory:
            if not self.victory_sound_played:
                self.assets.tingle_sound.play()
                self.victory_sound_played = True

            GameState.__blit_text_at_center(screen, self.assets.victory_text)

    @staticmethod
    def __blit_text_at_center(screen: pygame.Surface, text: pygame.Surface):
        screen.blit(
            text,
            (
                screen.get_width() // 2 - text.get_width() // 2,
                screen.get_height() // 2 - text.get_height() // 2,
            ),
        )
