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
        image: pygame.surface.Surface,
        rect: Optional[pygame.rect.Rect] = None,
    ):
        """
        Initialize GameObject class
        """
        if rect is None:
            rect = image.get_rect()
        self.image = image
        self.rect = rect
        self.game_state = game_state

    def remove(self):
        """
        Removes the GameObject
        """

    def events(self, events: list[pygame.event.Event]):
        """
        GameObject process events
        """

    def update(self):
        """
        Runs an update operation
        """

    def render(self, screen: pygame.Surface):
        """
        Render the GameObject onto the screen
        """
        if self.image is not None and self.rect is not None:
            screen.blit(self.image, self.rect)
