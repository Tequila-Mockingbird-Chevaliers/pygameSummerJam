import pygame


class GameObject:
    def __init__(self, game, image: pygame.Surface = None, rect: pygame.Rect = None):
        self.game = game
        self.image = image
        self.rect = rect

    def events(self, events):
        pass

    def update(self):
        pass

    def render(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
