import pygame

from src import constants as const
from src.scenes import GameScene, SceneManager
from src.state import GameState


class SpaceBreaker:
    """
    SpaceBreaker game class
    """

    def __init__(self):
        """
        Start the game
        """
        self.screen = pygame.display.set_mode(const.WINDOW_SIZE, pygame.SCALED)

        pygame.mixer.music.load(str(const.SOUNDS_FOLDER / "brecan_bgm.ogg"))
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(const.BG_MUSIC_VOL)

        self.game_state = GameState()
        self.manager = SceneManager()
        self.manager.go_to(GameScene(self.game_state))

    def run(self):
        """
        Run the game
        """
        clock = pygame.time.Clock()
        while True:
            if pygame.event.get(pygame.QUIT):
                self.quit()

            if self.manager.scene is not None:
                self.manager.scene.events(pygame.event.get())
                self.manager.scene.update()
                self.manager.scene.render(self.screen)

            pygame.display.flip()
            pygame.display.set_caption(f"BrickBrecan @ {clock.get_fps():.2f} FPS")
            clock.tick(const.FPS)

    def quit(self):
        """
        Quit the game
        """
        raise SystemExit(0)
