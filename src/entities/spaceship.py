import random

import src.constants as const
from src.entities.game_object import GameObject
from src.entities.laser import Laser
from src.state import GameState
from src.timer import Timer


class Spaceship(GameObject):
    """
    Spaceship class
    """

    def __init__(self, game_state: GameState, location: int):
        """
        Initialize Spaceship class
        """
        super().__init__(game_state, random.choice(game_state.assets.spaceships))
        self.rect.topleft = (location * const.SPACESHIP_WIDTH, -const.SPACESHIP_HEIGHT)
        self.line = location
        self.shoot_timer = Timer(const.SPACESHIP_SHOOT_TIMER, start=False)

    def update(self):
        """
        Runs an update operation
        """
        if self.rect.centery < 100:
            self.rect.centery += 1
            if self.rect.centery == 95:
                self.shoot_timer.start_timer()

        if self.shoot_timer.check_time():
            self.game_state.add_object("lasers", Laser(self.game_state, self))
            self.game_state.assets.laser_sound.play()
