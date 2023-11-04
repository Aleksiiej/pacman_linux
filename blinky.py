import pygame
from ghost import Ghost
from globalValues import *


class Blinky(Ghost):
    def __init__(self, width, height, posX, posY, isCheckbox=True):
        super().__init__(width, height, posX, posY)
        if isCheckbox == False:
            self.image = pygame.transform.scale(
                pygame.image.load(f"assets/ghost_images/red.png"), (50, 50)
            )
        self.currentDir = Direction.RIGHT
        self.restrictedDir = Direction.RIGHT
        self.ghostState = GhostStates.InBox

