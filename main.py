import pygame

from src import SpaceBreaker


if __name__ == "__main__":
    pygame.init()
    game = SpaceBreaker()
    game.run()
    pygame.quit()
