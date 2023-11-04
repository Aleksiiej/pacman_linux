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

    def update(self, walls, pacman):
        for _ in range(VELOCITY):
            possibleDirections = self.createListWithPossibleDirections(pacman, walls)

            if self.ghostState == GhostStates.InBox and len(possibleDirections) == 2:
                self.currentDir = Direction.UP
                self.restrictedDir = Direction.DOWN
                self.ghostState = GhostStates.Chasing
            elif len(possibleDirections) > 0:
                self.currentDir = min(possibleDirections, key=possibleDirections.get)

            self.setRestrictedDir()
            self.move(self)
            self.transferPosToOppositeSide()
