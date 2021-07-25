import pygame
import src.constants as const
import src.scenes as scenes


class SpaceBreaker:
    def __init__(self):
        self.screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
        self.manager = scenes.SceneManager(self)
        self.manager.go_to(scenes.GameScene())
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            if pygame.event.get(pygame.QUIT):
                self.quit()
            self.manager.scene.events(pygame.event.get())
            self.manager.scene.update()
            self.manager.scene.render(self.screen)
            pygame.display.flip()
            self.clock.tick(const.FPS)

    def quit(self):
        raise SystemExit


if __name__ == "__main__":
    pygame.init()
    game = SpaceBreaker()
    game.run()
