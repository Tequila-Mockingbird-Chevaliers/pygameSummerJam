import os
import sys

WIDTH = 600
HEIGHT = 900
FPS = 60

BALL_SPEED = 10
PADDLE_SPEED = 5

FOLDER = os.path.dirname(sys.modules["__main__"].__file__)
IMAGE_FOLDER = os.path.join(FOLDER, 'Assets\\Images')

PADDLE_IMAGE = 'Paddle.png'
BALL_IMAGE = 'Ball.png'
BRICK_IMAGE = 'Brick.png'
NO_OF_BRICK_IMAGES = 3
