import pygame
import time

import math

from src.constants import TIMER_BETWEEN_LEVELS
from src.entities.object_manager import ObjectManager
from src.assets import Assets
from src.timer import Timer


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
        self.timer_before_next_level = Timer(TIMER_BETWEEN_LEVELS, False)
        self.score: int = 0
        self.game_finished: bool = False
        self.init_game()

    def init_game(self):
        """
        Start a new level
        """
        self.timer_before_next_level.stop_timer()
        self.start_time: float = 0
        self.lives: int = 3
        self.in_play: bool = False
        self.defeat: bool = False
        self.victory: bool = False
        self.victory_sound_played = False

    def start(self):
        """
        Start a game
        """
        self.start_time: float = time.perf_counter()
        self.in_play: bool = True

    def add_score(self):
        """
        Update player score
        """
        div = max(math.sqrt(time.perf_counter() - self.start_time), 1)
        self.score += int(15 / div) + 3

    def update(self):
        if not self.victory and not self.defeat:
            super().update()
        if self.timer_before_next_level.check_time():
            self.timer_before_next_level.stop_timer()
            return True
        return False

    def render(self, screen: pygame.Surface):
        """
        Render GameState
        """
        super().render(screen)
        score_text = self.assets.score_font.render(
            f"SCORE : {self.score}", True, pygame.Color("white")
        )
        screen.blit(score_text, (0, self.assets.score_font.get_height() // 2))
        if self.defeat:
            GameState.__blit_text_at_center(screen, self.assets.defeat_text)

        elif self.victory:
            if not self.victory_sound_played:
                self.assets.tingle_sound.play()
                self.victory_sound_played = True

            if self.game_finished:
                GameState.__blit_text_at_center(screen, self.assets.game_completed_text)
            else:
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
