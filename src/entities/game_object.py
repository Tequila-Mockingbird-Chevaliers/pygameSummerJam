from __future__ import annotations

from typing import Optional, TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from src.state.game_state import GameState


class GameObject:
    """
    GameObject base class
    """

    def __init__(
        self,
        game_state: GameState,
        image: Optional[pygame.surface.Surface] = None,
        rect: Optional[pygame.rect.Rect] = None,
    ):
        if rect is None:
            rect = image.get_rect()
        self.image = image
        self.rect = rect
        self.game_state = game_state

    def remove(self):
        pass

    def events(self, events: list[pygame.event.Event]):
        pass

    def update(self):
        pass

    def render(self, screen: pygame.Surface):
        if self.image is not None and self.rect is not None:
            screen.blit(self.image, self.rect)
