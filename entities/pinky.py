import pygame
from entities.ghost import Ghost
from globalValues import *


class Pinky(Ghost):
    def __init__(self, width, height, posX, posY, isCheckbox=True):
        super().__init__(width, height, posX, posY)
        if isCheckbox == False:
            self.image = pygame.transform.scale(
                pygame.image.load(f"assets/ghost_images/pink.png"),
                (ENTITY_SIZE, ENTITY_SIZE),
            )
        self.restrictedDir = Direction.RIGHT
        self.FPSCounter = 0

    def update(self, walls, pacman):
        for _ in range(VELOCITY):
            if (self.FPSCounter % 4) == 0:
                self.updateFPSCounter()
            else:
                possibleDirections = self.createListWithPossibleDirections(
                    pacman, walls
                )
                if len(possibleDirections) > 0:
                    self.currentDir = min(
                        possibleDirections, key=possibleDirections.get
                    )
                self.setRestrictedDir()
                self.move(self)
                self.transferPosToOppositeSide()
                self.updateFPSCounter()
