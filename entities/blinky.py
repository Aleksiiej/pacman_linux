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
        self.restrictedDir = Direction.RIGHT
        self.FPSCounter = 0

    def update(self, walls, pacman):
        match self.ghostState:
            case GhostStates.Chase:
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
            case GhostStates.Scatter:
                # TODO
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

                pass
            case GhostStates.Frightened:
                # TODO
                # swapDir = self.currentdDir
                # self.currentDir = self.restrictedDir
                # self.restrictedDir = swapDir

                # for _ in range(VELOCITY):
                #     if (self.FPSCounter % 4) == 0:
                #         self.updateFPSCounter()

                pass
            case GhostStates.Eaten:
                # TODO
                pass
