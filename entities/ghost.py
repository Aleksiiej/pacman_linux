from entities.entity import Entity
from math import hypot
from globalValues import *


class Ghost(Entity):
    def __init__(self, width, height, posX, posY):
        super().__init__(width, height, posX, posY)
        self.ghostState = GhostStates.Chase

    def moveCheckbox(self, entity):
        match entity.currentDir:
            case Direction.LEFT:
                entity.rect.centerx -= 10
            case Direction.RIGHT:
                entity.rect.centerx += 10
            case Direction.UP:
                entity.rect.centery -= 10
            case Direction.DOWN:
                entity.rect.centery += 10

    def createCheckbox(self):
        return Ghost(
            self.rect.width,
            self.rect.height,
            self.rect.centerx,
            self.rect.centery,
        )

    def calculateDistance(self, pacman, checkbox):
        return hypot(
            pacman.rect.centerx - checkbox.rect.centerx,
            pacman.rect.centery - checkbox.rect.centery,
        )
    
    def calculateDistanceWhenScatter(self, checkbox):
        return hypot(
            760 - checkbox.rect.centerx,
            20 - checkbox.rect.centery,
        )
    

    def setRestrictedDir(self):
        match self.currentDir:
            case Direction.UP:
                self.restrictedDir = Direction.DOWN
            case Direction.DOWN:
                self.restrictedDir = Direction.UP
            case Direction.LEFT:
                self.restrictedDir = Direction.RIGHT
            case Direction.RIGHT:
                self.restrictedDir = Direction.LEFT

    def createListWithPossibleDirections(self, pacman, walls):
        possibleDirections = {}
        for dir in DIRECTION_LIST:
            checkbox = self.createCheckbox()
            checkbox.currentDir = dir
            self.moveCheckbox(checkbox)
            if not checkbox.checkCollisionWithWalls(checkbox, walls):
                if self.ghostState == GhostStates.Chase:
                    possibleDirections[dir] = self.calculateDistance(pacman, checkbox)
                elif self.ghostState == GhostStates.Scatter:
                    possibleDirections[dir] = self.calculateDistanceWhenScatter(checkbox)
            if self.restrictedDir in possibleDirections:
                del possibleDirections[self.restrictedDir]
        return possibleDirections

    def updateFPSCounter(self):
        if self.FPSCounter == 60:
            self.FPSCounter = 0
        self.FPSCounter += 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
