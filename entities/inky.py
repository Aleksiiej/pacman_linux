import pygame
from entities.ghost import Ghost
from globalValues import *
from math import hypot


class Inky(Ghost):
    def __init__(self, width, height, posX, posY, isCheckbox=True):
        super().__init__(width, height, posX, posY)
        if isCheckbox == False:
            self.image_ = pygame.transform.scale(
                pygame.image.load(f"assets/ghost_images/blue.png"),
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
        self.restrictedDir_ = Direction.LEFT
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
        pointAheadPacmanX, pointAheadPacmanY = 0, 0
        match pacman.currentDir_:
            case Direction.UP: 
                pointAheadPacmanX = pacman.rect.centerx
                pointAheadPacmanY = pacman.rect.centery - ENTITY_SIZE * 2
            case Direction.DOWN: 
                pointAheadPacmanX = pacman.rect.centerx
                pointAheadPacmanY = pacman.rect.centery + ENTITY_SIZE * 2
            case Direction.RIGHT: 
                pointAheadPacmanX = pacman.rect.centerx + ENTITY_SIZE * 2
                pointAheadPacmanY = pacman.rect.centery
            case Direction.LEFT: 
                pointAheadPacmanX = pacman.rect.centerx - ENTITY_SIZE * 2
                pointAheadPacmanY = pacman.rect.centery
                
        distX = pointAheadPacmanX - checkbox.rect.centerx
        distY = pointAheadPacmanY - checkbox.rect.centery

        destX = pointAheadPacmanX + distX
        destY = pointAheadPacmanY + distY

        return hypot(
            destX - checkbox.rect.centerx,
            destY - checkbox.rect.centery,
        )

    def calculateDistanceWhenScatter(self, checkbox):
        return hypot(
            PINKY_SCATTER_X - checkbox.rect.centerx,
            PINKY_SCATTER_Y - checkbox.rect.centery,
        )
