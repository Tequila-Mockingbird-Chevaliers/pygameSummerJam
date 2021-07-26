from abc import ABC, abstractmethod
from src.state.game_state import GameState

from src.entities.object_manager import ObjectManager


class Scene(ABC):
    def __init__(self, game_state: GameState):
        self.game_state = game_state

    def start(self):
        pass

    @abstractmethod
    def events(self, events):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    def end(self):
        self.game_state.clear_objects()
