from enum import Enum

SCREENSIZE = (1060, 840)
FPS = 60

ENTITY_SIZE = 40
APPLE_SIZE = 15
POWERUP_SIZE = 20

PACMAN_START_X = 380
PACMAN_START_Y = 620
BLINKY_START_X = 380
BLINKY_START_Y = 300
BLINKY_SCATTER_X = 760
BLINKY_SCATTER_Y = 20
PINKY_START_X = 380
PINKY_START_Y = 380
PINKY_SCATTER_X = 80
PINKY_SCATTER_Y = 20
INKY_START_X = 340
INKY_START_Y = 380
INKY_SCATTER_X = 760
INKY_SCATTER_Y = 760
CLYDE_START_X = 420
CLYDE_START_Y = 380
CLYDE_SCATTER_X = 20
CLYDE_SCATTER_Y = 760

HOUSE_X = 380
HOUSE_Y = 380

CHASE_TIME = 20
SCATTER_TIME = 7
FRIGHTENED_TIME = 6

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


DIRECTION_LIST = {Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT}


class GhostStates(Enum):
    InBox = 0
    Chase = 1
    Scatter = 2
    Frightened = 3
    Eaten = 4
    Wait = 5


mapInit = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 3, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 3, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 2, 1, 1, 1, 0, 1, 0, 1, 1, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 0, 1, 1, 0, 1, 1, 0, 1, 2, 1, 1, 1, 1],
    [0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0],
    [1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 2, 1],
    [1, 2, 2, 1, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 1],
    [1, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 2, 1, 2, 1, 1],
    [1, 2, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2, 2, 1],
    [1, 3, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1, 1, 3, 1],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# 0 - nothing
# 1 - wall
# 2 - apple
# 3 - powerUp
