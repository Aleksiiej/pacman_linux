from entities.entity import Entity
from globalValues import *
import random
from math import hypot


class Ghost(Entity):
    def __init__(self, width, height, posX, posY):
        super().__init__(width, height, posX, posY)

    def update(self, walls, pacman):
        for _ in range(VELOCITY):
            if (self.FPSCounter % 4) == 0:
                self.updateFPSCounter()
            else:
                possibleDirections = self.createListWithPossibleDirections(
                    pacman, walls
                )
                if self.rect.centerx == HOUSE_X and self.rect.centery == HOUSE_Y:
                    self.currentDir_ = Direction.UP
                elif (
                    self.rect.centerx == BLINKY_START_X
                    and self.rect.centery == BLINKY_START_Y
                    and self.currentDir_ == Direction.LEFT
                    and self.ghostState != GhostStates.Eaten
                ):
                    self.currentDir_ = Direction.LEFT
                elif (
                    self.rect.centerx == BLINKY_START_X
                    and self.rect.centery == BLINKY_START_Y
                    and self.currentDir_ == Direction.RIGHT
                    and self.ghostState != GhostStates.Eaten
                ):
                    self.currentDir_ = Direction.RIGHT
                elif len(possibleDirections) > 0:
                    self.currentDir_ = min(
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
            checkbox.currentDir_ = dir
            self.moveCheckbox(checkbox)
            if not checkbox.checkCollisionWithWalls(checkbox, walls):
                match self.ghostState:
                    case GhostStates.InBox:
                        possibleDirections[dir] = self.calculateDistanceWhenInBox(
                            checkbox
                        )
                    case GhostStates.Chase:
                        possibleDirections[dir] = self.calculateDistanceWhenChase(
                            pacman, checkbox
                        )
                    case GhostStates.Scatter:
                        possibleDirections[dir] = self.calculateDistanceWhenScatter(
                            checkbox
                        )
                    case GhostStates.Frightened:
                        possibleDirections[dir] = self.calculateRandomDir()
                    case GhostStates.Eaten:
                        possibleDirections[dir] = self.calculateDistanceWhenEaten(
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
        match entity.currentDir_:
            case Direction.LEFT:
                entity.rect.centerx -= 10
            case Direction.RIGHT:
                entity.rect.centerx += 10
            case Direction.UP:
                entity.rect.centery -= 10
            case Direction.DOWN:
                entity.rect.centery += 10

    def calculateRandomDir(self):
        return random.randrange(0, 100)

    def calculateDistanceWhenEaten(self, checkbox):
        if checkbox.rect.centerx == HOUSE_X and checkbox.rect.centery == HOUSE_Y:
            self.ghostState = GhostStates.Chase
        return hypot(
            HOUSE_X - checkbox.rect.centerx,
            HOUSE_Y - checkbox.rect.centery,
        )

    def setRestrictedDir(self):
        match self.currentDir_:
            case Direction.UP:
                self.restrictedDir = Direction.DOWN
            case Direction.DOWN:
                self.restrictedDir = Direction.UP
            case Direction.LEFT:
                self.restrictedDir = Direction.RIGHT
            case Direction.RIGHT:
                self.restrictedDir = Direction.LEFT

    def reverseDir(self):
        match self.currentDir_:
            case Direction.UP:
                self.currentDir_ = Direction.DOWN
                self.restrictedDir = Direction.UP
            case Direction.DOWN:
                self.currentDir_ = Direction.UP
                self.restrictedDir = Direction.DOWN
            case Direction.LEFT:
                self.currentDir_ = Direction.RIGHT
                self.restrictedDir = Direction.LEFT
            case Direction.RIGHT:
                self.currentDir_ = Direction.LEFT
                self.restrictedDir = Direction.RIGHT

    def draw(self, screen):
        match self.ghostState:
            case GhostStates.InBox:
                screen.blit(self.image_, (self.rect.x, self.rect.y))
            case GhostStates.Chase:
                screen.blit(self.image_, (self.rect.x, self.rect.y))
            case GhostStates.Scatter:
                screen.blit(self.image_, (self.rect.x, self.rect.y))
            case GhostStates.Frightened:
                screen.blit(self.frightenedImage_, (self.rect.x, self.rect.y))
            case GhostStates.Eaten:
                screen.blit(self.eatenImage_, (self.rect.x, self.rect.y))
