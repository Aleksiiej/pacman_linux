from entities.entity import Entity
from math import hypot
from globalValues import *


class Ghost(Entity):
    def __init__(self, width, height, posX, posY):
        super().__init__(width, height, posX, posY)
        self.ghostState = GhostStates.Chase

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

    def updateFPSCounter(self):
        if self.FPSCounter == 60:
            self.FPSCounter = 0
        self.FPSCounter += 1

    def createListWithPossibleDirections(self, pacman, walls):
        possibleDirections = {}
        for dir in DIRECTION_LIST:
            checkbox = self.createCheckbox()
            checkbox.currentDir = dir
            self.moveCheckbox(checkbox)
            if not checkbox.checkCollisionWithWalls(checkbox, walls):
                match self.ghostState:
                    case GhostStates.Chase:
                        possibleDirections[dir] = self.calculateDistanceWhenChase(
                            pacman, checkbox
                        )
                    case GhostStates.Scatter:
                        possibleDirections[dir] = self.calculateDistanceWhenScatter(
                            checkbox
                        )
            if self.restrictedDir in possibleDirections:
                del possibleDirections[self.restrictedDir]
        return possibleDirections

    def createCheckbox(self):
        return Ghost(
            self.rect.width,
            self.rect.height,
            self.rect.centerx,
            self.rect.centery,
        )

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

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
