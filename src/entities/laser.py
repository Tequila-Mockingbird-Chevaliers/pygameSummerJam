from src.entities.game_object import GameObject
import src.constants as const


class Laser(GameObject):
    def __init__(self, game, spaceship):
        image = game.program.assets.images['LASER']
        rect = image.get_rect()
        rect.center = spaceship.rect.center
        super().__init__(game, image, rect)

    def update(self):
        self.rect.y += const.LASER_SPEED
        if self.rect.y > const.HEIGHT + 50:
            self.remove()
