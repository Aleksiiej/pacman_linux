from enum import Enum

SCREENSIZE = (900, 900)

FPS = 60

VELOCITY = 4

BLACK = (0, 0, 0) 
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4    