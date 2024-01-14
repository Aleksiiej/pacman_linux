import pygame
from entities.ghost import Ghost
from globalValues import *
from math import hypot


class Clyde(Ghost):
    def __init__(self, width, height, posX, posY, isCheckbox=True):
        super().__init__(width, height, posX, posY)
        if isCheckbox == False:
            self.image_ = pygame.transform.scale(
                pygame.image.load(f"assets/ghost_images/orange.png"),
                (ENTITY_SIZE, ENTITY_SIZE),
            )
            self.frightenedImage_ = pygame.transform.scale(
                pygame.image.load(f"assets/ghost_images/powerup.png"),
                (ENTITY_SIZE, ENTITY_SIZE),
            )
            self.eatenImage_ = pygame.transform.scale(
                pygame.image.load(f"assets/ghost_images/dead.png"),
                (ENTITY_SIZE, ENTITY_SIZE),
            )
        self.restrictedDir_ = Direction.RIGHT
        self.FPSCounter_ = 0
        self.ghostState_ = GhostStates.Wait

    def calculateDistanceWhenInBox(self, checkbox):
        if self.rect.centery < 380:
            self.ghostState_ = GhostStates.Scatter
        return hypot(
            380 - checkbox.rect.centerx,
            340 - checkbox.rect.centery,
        )

    def calculateDistanceWhenChase(self, pacman, checkbox):
        return hypot(
            pacman.rect.centerx - checkbox.rect.centerx,
            pacman.rect.centery - checkbox.rect.centery,
        )

    def calculateDistanceWhenScatter(self, checkbox):
        return hypot(
            CLYDE_SCATTER_X - checkbox.rect.centerx,
            CLYDE_SCATTER_Y - checkbox.rect.centery,
        )
