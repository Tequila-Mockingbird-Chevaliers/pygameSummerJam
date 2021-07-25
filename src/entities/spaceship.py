from src.timer import Timer
from src.entities.game_object import GameObject
import src.constants as const
from src.entities.laser import Laser


class Spaceship(GameObject):
    def __init__(self, game, location):
        image = game.program.assets.images['SPACESHIP']
        rect = image.get_rect()
        rect.center = (50 + location * 100, -50)
        super().__init__(game, image, rect)
        self.shoot_timer = Timer(const.SPACESHIP_SHOOT_TIMER, start=False)

    def update(self):
        if self.rect.centery < 100:
            self.rect.centery += 1
            if self.rect.centery == 95:
                self.shoot_timer.start_timer()
        if self.shoot_timer.check_time():
            self.game.object_manager.add_object('lasers', Laser(self.game, self))
