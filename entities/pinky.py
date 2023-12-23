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
        return hypot(
            pacman.rect.centerx - checkbox.rect.centerx,
            pacman.rect.centery - checkbox.rect.centery,
        )

    def calculateDistanceWhenScatter(self, checkbox):
        return hypot(
            PINKY_SCATTER_X - checkbox.rect.centerx,
            PINKY_SCATTER_Y - checkbox.rect.centery,
        )
