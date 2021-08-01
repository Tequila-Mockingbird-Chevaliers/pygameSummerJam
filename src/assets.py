from __future__ import annotations

from typing import Optional

import pygame

import src.constants as const


def load_image(
    image_name: str,
    transparent_color=None,
    alpha: Optional[int] = None,
    size: Optional[tuple[int, int]] = None,
):
    """
    Utility function to load an image, also handles transparancy
    """
    image = pygame.image.load(const.IMAGE_FOLDER / image_name)

    if size is not None:
        image = pygame.transform.scale(image, size)

    if transparent_color is not None:
        image.set_colorkey(transparent_color)

    if alpha is not None:
        image.set_alpha(alpha)

    return image.convert_alpha()


class Assets:
    """
    A data container class to store assets
    """

    def __init__(self):
        self.bg_images = [
            load_image(f"{const.BG_IMAGE}{i}.{const.BG_IMAGE_EXT}")
            for i in range(1, const.NO_OF_BGS + 1)
        ]

        self.paddle = load_image(const.PADDLE_IMAGE)
        self.ball = load_image(const.BALL_IMAGE)

        self.bricks = [
            load_image(
                f"{const.BRICK_IMAGE}{i}.{const.BRICK_IMAGE_EXT}",
                size=(const.BRICK_WIDTH, const.BRICK_HEIGHT),
            )
            for i in range(1, const.NO_OF_BRICK_IMAGES + 1)
        ]

        self.spaceships = [
            load_image(
                f"{const.SPACESHIP_IMAGE}{i}.{const.SPACESHIP_IMAGE_EXT}",
                size=(const.SPACESHIP_WIDTH, const.SPACESHIP_HEIGHT),
            )
            for i in range(1, const.NO_OF_SPACESHIPS + 1)
        ]

        self.laser = load_image(const.LASER_IMAGE, transparent_color=(255, 255, 255))

        self.score_font = pygame.font.Font(pygame.font.get_default_font(), 20)

        default_font = pygame.font.Font(pygame.font.get_default_font(), 50)
        self.defeat_text = default_font.render("GAME OVER", True, pygame.Color("white"))
        self.victory_text = default_font.render(
            "VICTORY !", True, pygame.Color("white")
        )

        self.laser_sound = pygame.mixer.Sound(const.SOUNDS_FOLDER / "pew.ogg")
        self.block_sound = pygame.mixer.Sound(const.SOUNDS_FOLDER / "blop.ogg")

        self.paddle_sound = pygame.mixer.Sound(const.SOUNDS_FOLDER / "blam.ogg")
        self.tingle_sound = pygame.mixer.Sound(const.SOUNDS_FOLDER / "tingle.ogg")
