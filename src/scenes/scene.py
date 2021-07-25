from abc import ABC, abstractmethod

from src import object_manager


class Scene(ABC):
    def __init__(self, program):
        self.program = program
        self.object_manager: object_manager.ObjectManager = (
            object_manager.ObjectManager(self.program)
        )

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
        self.object_manager.clear_objects()
