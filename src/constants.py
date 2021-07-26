import os
import sys

WIDTH = 600
HEIGHT = 900
FPS = 60

BALL_SPEED = 10
PADDLE_SPEED = 8
SPACESHIP_SPAWN_TIMER = 5000
SPACESHIP_SHOOT_TIMER = 2350
LASER_SPEED = 7

FOLDER = os.path.dirname(sys.modules["__main__"].__file__)
IMAGE_FOLDER = os.path.join(FOLDER, 'Assets\\Images')

PADDLE_IMAGE = 'Paddle.png'
BALL_IMAGE = 'Ball.png'
BRICK_IMAGE = 'Brick.png'
NO_OF_BRICK_IMAGES = 3
SPACESHIP_IMAGE = 'Spaceship.png'
LASER_IMAGE = 'Laser.png'
