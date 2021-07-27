from __future__ import annotations

import pygame

from src.entities.game_object import GameObject


class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ObjectGroup:
    """
    ObjectGroup class
    """

    def __init__(self):
        """
        Initialize ObjectGroup class
        """
        self.objects: list[GameObject] = []

    def __iter__(self):
        """
        Iterate over objects in the group
        """
        return self.objects.__iter__()

    def add(self, obj):
        """
        Add an object to a group
        """
        self.objects.append(obj)

    def events(self, events: list[pygame.event.Event]):
        """
        Feed game events into every object
        """
        for obj in self.objects:
            obj.events(events)

    def update(self):
        """
        Update all objects in the group
        """
        for obj in self.objects:
            obj.update()

    def render(self, screen: pygame.Surface):
        """
        Render all objects in the group
        """
        for obj in self.objects:
            obj.render(screen)

    def remove_object(self, obj: GameObject):
        """
        Remove an object from the group if it is a part of it. Returns whether
        the object was successfully removed or not.
        """
        if obj not in self.objects:
            return False

        obj.remove()
        self.objects.remove(obj)
        return True


class ObjectManager(metaclass=_Singleton):
    """
    ObjectManager class
    """

    def __init__(self):
        """
        Initialize ObjectManager class
        """
        self.objects: dict[str, ObjectGroup] = {}

    def __getitem__(self, name: str) -> GameObject:
        """
        Gets the first GameObject that belongs to the particular ObjectGroup
        """
        return self.objects[name].objects[0]

    def add_object(self, name: str, obj: GameObject):
        """
        Add GameObject to ObjectManager
        """
        if name not in self.objects:
            self.objects[name] = ObjectGroup()

        self.objects[name].add(obj)
        return obj

    def remove_object(self, obj: GameObject):
        """
        Remove GameObject from ObjectManager
        """
        for group in self.objects.values():
            group.remove_object(obj)
            if group.remove_object(obj):
                return

    def clear_objects(self):
        """
        Clear all objects
        """
        self.objects.clear()

    def get_number_of_objects(self, name: str):
        """
        Get number of objects
        """
        return len(self.objects[name].objects)

    def events(self, events: list[pygame.event.Event]):
        """
        Process events
        """
        for group in self.objects.values():
            group.events(events)

    def update(self):
        """
        Update GameObjects
        """
        for group in list(self.objects.values()):
            group.update()

    def render(self, screen: pygame.Surface):
        """
        Render GameObjects
        """
        for group in self.objects.values():
            group.render(screen)

    def test_collision(self, first: str, second: str, function):
        """
        Test for collision between groups of objects
        """
        first_group = self.objects[first]
        second_group = self.objects[second]
        for first_obj in first_group:
            if first_obj.rect is None:
                continue

            for second_obj in second_group:
                if second_obj.rect is not None and first_obj.rect.colliderect(
                    second_obj.rect
                ):
                    function([first_obj, second_obj])
