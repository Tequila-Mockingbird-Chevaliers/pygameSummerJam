import sys

from pathlib import Path

WIDTH = 360
HEIGHT = 600
WINDOW_SIZE = (WIDTH, HEIGHT)
FPS = 60

BLOCK_WIDTH = 30
BLOCK_HEIGHT = 20
SPACESHIP_WIDTH = 60
SPACESHIP_HEIGHT = 60
BRICK_WIDTH = BLOCK_WIDTH
BRICK_HEIGHT = BLOCK_HEIGHT

BALL_SPEED = 8
PADDLE_SPEED = 8
SPACESHIP_SPAWN_TIMER = 3500
SPACESHIP_SHOOT_TIMER = 2350
LASER_SPEED = 7

MAX_LEVEL = 3
TIMER_BETWEEN_LEVELS = 2000

MAIN_FOLDER = Path(sys.argv[0]).parent
ASSETS_FOLDER = MAIN_FOLDER / "assets"
IMAGE_FOLDER = ASSETS_FOLDER / "images"
SOUNDS_FOLDER = ASSETS_FOLDER / "sounds"

LEVELS_FOLDER = MAIN_FOLDER / "levels"

FONT_FILE = ASSETS_FOLDER / "Asimov.otf"

PADDLE_IMAGE = "Paddle.png"
BALL_IMAGE = "Ball.png"
LASER_IMAGE = "Laser.png"

BRICK_IMAGE = "Brick"
SPACESHIP_IMAGE = "spaceship"
BG_IMAGE = "bg"
BRICK_IMAGE_EXT = SPACESHIP_IMAGE_EXT = BG_IMAGE_EXT = "png"

NO_OF_BRICK_IMAGES = 5
NO_OF_SPACESHIPS = 2
NO_OF_BGS = 1

BG_MUSIC_VOL = 0.75
