import pygame
from entities.ghost import Ghost
from globalValues import *
from math import hypot


class Blinky(Ghost):
    def __init__(self, width, height, posX, posY, isCheckbox=True):
        super().__init__(width, height, posX, posY)
        if isCheckbox == False:
            self.image_ = pygame.transform.scale(
                pygame.image.load(f"assets/ghost_images/red.png"),
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
        self.restrictedDir_ = Direction.DOWN
        self.FPSCounter_ = 0
        self.ghostState_ = GhostStates.Scatter

    def calculateDistanceWhenChase(self, pacman, checkbox):
        return hypot(
            pacman.rect.centerx - checkbox.rect.centerx,
            pacman.rect.centery - checkbox.rect.centery,
        )

    def calculateDistanceWhenScatter(self, checkbox):
        return hypot(
            BLINKY_SCATTER_X - checkbox.rect.centerx,
            BLINKY_SCATTER_Y - checkbox.rect.centery,
        )
