import pygame
from entities.ghost import Ghost
from globalValues import *
from math import hypot


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

    def calculateDistanceWhenChase(self, pacman, checkbox):
        expectedPointX = pacman.rect.centerx
        expectedPointY = pacman.rect.centery

        match pacman.currentDir:
            case Direction.UP:
                expectedPointY -= 4.5 * ENTITY_SIZE
            case Direction.DOWN:
                expectedPointY += 4.5 * ENTITY_SIZE
            case Direction.RIGHT:
                expectedPointX += 4.5 * ENTITY_SIZE
            case Direction.LEFT:
                expectedPointY -= 4.5 * ENTITY_SIZE

        return hypot(
            expectedPointX - checkbox.rect.centerx,
            expectedPointY - checkbox.rect.centery,
        )

    def calculateDistanceWhenScatter(self, checkbox):
        return hypot(
            PINKY_SCATTER_X - checkbox.rect.centerx,
            PINKY_SCATTER_Y - checkbox.rect.centery,
        )
