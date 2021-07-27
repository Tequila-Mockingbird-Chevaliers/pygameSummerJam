from __future__ import annotations

from typing import TYPE_CHECKING

import src.constants as const
from src.entities.game_object import GameObject
from src.state.game_state import GameState

if TYPE_CHECKING:
    from src.entities.spaceship import Spaceship


class Laser(GameObject):
    """
    Laser class
    """

    def __init__(self, game_state: GameState, spaceship: Spaceship):
        """
        Initialize Laser class
        """
        super().__init__(game_state, game_state.assets.laser)
        self.rect.center = spaceship.rect.center

    def update(self):
        """
        Runs an update operation
        """
        self.rect.y += const.LASER_SPEED
        if self.rect.y > const.HEIGHT + 50:
            self.remove()
