import src.constants as const
from src.entities.game_object import GameObject
from src.entities.laser import Laser
from src.state import GameState
from src.timer import Timer


class Spaceship(GameObject):
    def __init__(self, game_state: GameState, location: int):
        super().__init__(game_state, game_state.assets.spaceship)
        self.rect.center = (50 + location * 100, -50)
        self.shoot_timer = Timer(const.SPACESHIP_SHOOT_TIMER, start=False)

    def update(self):
        if self.rect.centery < 100:
            self.rect.centery += 1
            if self.rect.centery == 95:
                self.shoot_timer.start_timer()

        if self.shoot_timer.check_time():
            self.game_state.add_object("lasers", Laser(self.game_state, self))
