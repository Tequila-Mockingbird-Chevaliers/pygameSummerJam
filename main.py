import platform

import pygame
import src.constants as const
import src.scene_manager
import src.assets
import src.scenes.game_scene


class SpaceBreaker:
    def __init__(self):
        if platform.system() == 'Windows':
            from ctypes import windll
            try:
                windll.user32.SetProcessDPIAware()
            except AttributeError:
                pass
        self.screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT), pygame.SCALED)
        self.assets = src.assets.Assets()
        self.manager = src.scene_manager.SceneManager(self)
        self.manager.go_to(src.scenes.game_scene.GameScene(self))
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
            pygame.display.set_caption(f"{self.clock.get_fps()}")
            self.clock.tick(const.FPS)

    def quit(self):
        raise SystemExit


if __name__ == "__main__":
    pygame.init()
    game = SpaceBreaker()
    game.run()
