from typing import Dict


class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class ObjectGroup:
    def __init__(self):
        self.objects = []

    def __iter__(self):
        return self.objects.__iter__()

    def add(self, obj):
        self.objects.append(obj)

    def events(self, events):
        for obj in self.objects:
            obj.events(events)

    def update(self):
        for obj in self.objects:
            obj.update()

    def render(self, screen):
        for obj in self.objects:
            obj.render(screen)


class ObjectManager(metaclass=_Singleton):
    def __init__(self, program):
        self.program = program
        self.objects: Dict[str, ObjectGroup] = dict()

    def add_object(self, name, obj):
        if name not in self.objects:
            self.objects[name] = ObjectGroup()
        group = self.objects[name]
        group.add(obj)
        return obj

    def remove_object(self, obj):
        for group in self.objects.values():
            if obj in group.objects:
                group.objects.remove(obj)
                obj.remove()
                return

    def clear_objects(self):
        self.objects.clear()

    def get_number_of_objects(self, name):
        return len(self.objects[name].objects)

    def events(self, events):
        for group in self.objects.values():
            group.events(events)

    def update(self):
        for group in list(self.objects.values()):
            group.update()

    def render(self, screen):
        for group in self.objects.values():
            group.render(screen)

    def test_collision(self, first, second, function):
        first_group = self.objects[first]
        second_group = self.objects[second]
        for first_obj in first_group:
            for second_obj in second_group:
                if first_obj.rect.colliderect(second_obj.rect):
                    function([first_obj, second_obj])
