import pygame


class Timer:
    def __init__(self, countdown, start=True):
        self.countdown = countdown
        self.current_time = None
        self.last_update = None
        self.running = False
        if start:
            self.start_timer()

    def start_timer(self):
        self.running = True
        self.last_update = pygame.time.get_ticks()
        self.current_time = pygame.time.get_ticks()

    def stop_timer(self):
        self.running = False

    def check_time(self):
        if self.running:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.last_update > self.countdown:
                self.last_update = self.current_time
                return True
            else:
                return False
        return False

    def get_percentage(self):
        return (self.current_time - self.last_update) / self.countdown