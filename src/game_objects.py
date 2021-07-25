import random
import pygame
import constants as const


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


class Paddle(GameObject):
    def __init__(self, game):
        image = pygame.Surface((80, 30))
        image.fill("GREEN")
        rect = image.get_rect()
        rect.center = (const.WIDTH // 2, const.HEIGHT - 50)
        super().__init__(game, image, rect)
        self.direction = 0

    def events(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.direction == -1 or event.key == pygame.K_RIGHT and self.direction == 1:
                    self.direction = 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = -1
                if event.key == pygame.K_RIGHT:
                    self.direction = 1

    def update(self):
        if self.direction:
            self.rect.x += const.PADDLE_SPEED * self.direction
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.right > const.WIDTH:
                self.rect.right = const.WIDTH


class Ball(GameObject):
    def __init__(self, game):
        image = pygame.Surface((20, 20))
        image.set_colorkey("Black")
        pygame.draw.circle(image, "RED", (10, 10), 10)
        rect = image.get_rect()
        rect.center = (const.WIDTH // 2, const.HEIGHT - 75)
        super().__init__(game, image, rect)
        seed = random.choice([-1, 1]) * random.randint(1, 5)
        self.direction = pygame.Vector2(seed, random.randrange(2, 5) * abs(seed) * -1).normalize()

    def update(self):
        if not self.game.in_play:
            self.rect.centerx = self.game.paddle.rect.centerx
        else:
            if self.rect.x + self.direction.x * const.BALL_SPEED < 0 or self.rect.right + self.direction.x * const.BALL_SPEED > const.WIDTH:
                self.direction.x *= -1
            if self.rect.y + self.direction.y * const.BALL_SPEED < 0:
                self.direction.y *= -1
            self.rect.center += self.direction * const.BALL_SPEED
