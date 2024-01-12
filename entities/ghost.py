from entities.entity import Entity
from globalValues import *
import random
from math import hypot


class Ghost(Entity):
    def __init__(self, width, height, posX, posY):
        super().__init__(width, height, posX, posY)

    def update(self, walls, pacman):
        ghost_velocity = 3
        for _ in range(ghost_velocity):
            if (
                self.ghostState_ == GhostStates.Chase
                or self.ghostState_ == GhostStates.Scatter
                or self.ghostState_ == GhostStates.Eaten
                or self.ghostState_ == GhostStates.InBox
            ):
                if (self.FPSCounter_ % 4) == 0:
                    self.updateFPSCounter()
                else:
                    self.performMove(walls, pacman)
            elif self.ghostState_ == GhostStates.Frightened:
                if (self.FPSCounter_ % 2) == 0:
                    self.updateFPSCounter()
                else:
                    self.performMove(walls, pacman)
            elif self.ghostState_ == GhostStates.Wait:
                pass

    def performMove(self, walls, pacman):
        possibleDirections = self.createListWithPossibleDirections(pacman, walls)
        if self.rect.centerx == HOUSE_X and self.rect.centery == HOUSE_Y:
            self.currentDir_ = Direction.UP
        elif (
            self.rect.centerx == BLINKY_START_X
            and self.rect.centery == BLINKY_START_Y
            and self.currentDir_ == Direction.LEFT
            and self.ghostState_ != GhostStates.Eaten
        ):
            self.currentDir_ = Direction.LEFT
        elif (
            self.rect.centerx == BLINKY_START_X
            and self.rect.centery == BLINKY_START_Y
            and self.currentDir_ == Direction.RIGHT
            and self.ghostState_ != GhostStates.Eaten
        ):
            self.currentDir_ = Direction.RIGHT
        elif len(possibleDirections) > 0:
            self.currentDir_ = min(possibleDirections, key=possibleDirections.get)
        self.setRestrictedDir()
        self.move(self)
        self.transferPosToOppositeSide()
        self.updateFPSCounter()

    def updateFPSCounter(self):
        if self.FPSCounter_ == 60:
            self.FPSCounter_ = 0
        self.FPSCounter_ += 1

    def createListWithPossibleDirections(self, pacman, walls):
        possibleDirections = {}
        for dir in DIRECTION_LIST:
            checkbox = self.createCheckbox()
            checkbox.currentDir_ = dir
            self.moveCheckbox(checkbox)
            if not checkbox.checkCollisionWithWalls(checkbox, walls):
                match self.ghostState_:
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
            if self.restrictedDir_ in possibleDirections:
                del possibleDirections[self.restrictedDir_]
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
            self.ghostState_ = GhostStates.Chase
        return hypot(
            HOUSE_X - checkbox.rect.centerx,
            HOUSE_Y - checkbox.rect.centery,
        )

    def setRestrictedDir(self):
        match self.currentDir_:
            case Direction.UP:
                self.restrictedDir_ = Direction.DOWN
            case Direction.DOWN:
                self.restrictedDir_ = Direction.UP
            case Direction.LEFT:
                self.restrictedDir_ = Direction.RIGHT
            case Direction.RIGHT:
                self.restrictedDir_ = Direction.LEFT

    def reverseDir(self):
        match self.currentDir_:
            case Direction.UP:
                self.currentDir_ = Direction.DOWN
                self.restrictedDir_ = Direction.UP
            case Direction.DOWN:
                self.currentDir_ = Direction.UP
                self.restrictedDir_ = Direction.DOWN
            case Direction.LEFT:
                self.currentDir_ = Direction.RIGHT
                self.restrictedDir_ = Direction.LEFT
            case Direction.RIGHT:
                self.currentDir_ = Direction.LEFT
                self.restrictedDir_ = Direction.RIGHT

    def draw(self, screen):
        match self.ghostState_:
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
            case GhostStates.Wait:
                screen.blit(self.image_, (self.rect.x, self.rect.y))
