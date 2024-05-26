from enum import Enum

FPS = 60
WINDOW_SIZE = (WIDTH, HEIGHT) = (1080, 800)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class DIRECTION(Enum):
    LEFT = -1
    RIGHT = 1
    UP = -1
    DOWN = 1
