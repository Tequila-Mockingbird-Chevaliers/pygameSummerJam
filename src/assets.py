import os

import pygame

import src.constants as const


def load_image(image_name, transparent_color=None, alpha=None):
    image = pygame.image.load(os.path.join(const.IMAGE_FOLDER, image_name))
    if transparent_color:
        image.set_colorkey(transparent_color)
    if alpha:
        image.set_alpha(alpha)
    return image.convert_alpha()


class Assets:
    def __init__(self):
        self.images = {}
        self.load()

    def load(self):
        self.images["PADDLE"] = load_image(const.PADDLE_IMAGE)
        self.images["BALL"] = load_image(const.BALL_IMAGE, transparent_color=(0, 0, 0))
        for i in range(const.NO_OF_BRICK_IMAGES):
            print(f'{const.BRICK_IMAGE[:5] + str(i + 1) + const.BRICK_IMAGE[5:]}')
            self.images[f"BRICK{i}"] = load_image(f'{const.BRICK_IMAGE[:5] + str(i + 1) + const.BRICK_IMAGE[5:]}')
