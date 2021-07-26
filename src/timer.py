import pygame


class Timer:
    """
    Timer class
    """

    def __init__(self, countdown: int, start: bool = True):
        """
        Initialise timer instance
        """
        self.countdown = countdown
        self.last_update: int = 0
        self.current_time: int = 0
        self.running: bool = False
        if start:
            self.start_timer()

    def start_timer(self):
        """
        Start the timer
        """
        self.running = True
        self.last_update = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()

    def stop_timer(self):
        """
        Stop the timer
        """
        self.running = False

    def check_time(self):
        """
        Check the time
        """
        if not self.running:
            return False

        self.current_time = pygame.time.get_ticks()
        if self.current_time - self.last_update > self.countdown:
            self.last_update = self.current_time
            return True
        return False

    def get_percentage(self):
        """
        Get the time percentage
        """
        return (self.current_time - self.last_update) / self.countdown
