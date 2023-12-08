import pygame
from entities.ghost import Ghost
from globalValues import *


class Blinky(Ghost):
    def __init__(self, width, height, posX, posY, isCheckbox=True):
        super().__init__(width, height, posX, posY)
        if isCheckbox == False:
            self.image = pygame.transform.scale(
                pygame.image.load(f"assets/ghost_images/red.png"),
                (ENTITY_SIZE, ENTITY_SIZE),
            )
        self.currentDir = Direction.RIGHT
        self.restrictedDir = Direction.RIGHT
        self.ghostState = GhostStates.Chase
        self.FPSCounter = 0

    def update(self, walls, pacman):
        if self.ghostState == GhostStates.Chase:
            for _ in range(VELOCITY):
                if (self.FPSCounter % 4) == 0:
                    if self.FPSCounter == 60:
                        self.FPSCounter = 0
                    self.FPSCounter += 1
                    pass
                else:
                    possibleDirections = self.createListWithPossibleDirections(
                        pacman, walls
                    )

                    if (
                        self.ghostState == GhostStates.InBox
                        and len(possibleDirections) == 2
                    ):
                        self.currentDir = Direction.UP
                        self.restrictedDir = Direction.DOWN
                        self.ghostState = GhostStates.Chasing
                    elif len(possibleDirections) > 0:
                        self.currentDir = min(
                            possibleDirections, key=possibleDirections.get
                        )

                    self.setRestrictedDir()
                    self.move(self)
                    self.transferPosToOppositeSide()
                    if self.FPSCounter == 60:
                        self.FPSCounter = 0
                    self.FPSCounter += 1
