from entity import Entity
from globalValues import *


class Pacman(Entity):
    def __init__(self, width, height, posX, posY, color):
        super().__init__(width, height, posX, posY, color)

    def changeDir(self, newDir):
        self.proposedDir = newDir

    def move(self, entity):
        match entity.currentDir:
            case Direction.LEFT:
                entity.rect.x -= 1
            case Direction.RIGHT:
                entity.rect.x += 1
            case Direction.UP:
                entity.rect.y -= 1
            case Direction.DOWN:
                entity.rect.y += 1

    def createCheckbox(self):
        ret = Pacman(
            self.image.get_width(),
            self.image.get_height(),
            self.rect.centerx,
            self.rect.centery,
            BLACK,
        )
        ret.currentDir, ret.proposedDir = self.currentDir, self.proposedDir
        return ret

    def restoreCheckbox(self, checkbox):
        checkbox.currentDir = self.currentDir
        checkbox.proposedDir = self.proposedDir

    def checkCollisionWithWalls(self, checkbox, walls):
        for wall in walls:
            if checkbox.rect.colliderect(wall):
                return True
        return False

    def update(self, walls):
        checkbox = self.createCheckbox()
        for _ in range(VELOCITY):
            if self.currentDir == self.proposedDir:
                self.move(checkbox)
                if not self.checkCollisionWithWalls(checkbox, walls):
                    self.move(self)
            else:
                checkbox.currentDir = checkbox.proposedDir
                self.move(checkbox)
                if self.checkCollisionWithWalls(checkbox, walls):
                    checkbox = self.createCheckbox()
                    self.move(checkbox)
                    if not self.checkCollisionWithWalls(checkbox, walls):
                        self.move(self)
                else:
                    self.currentDir = self.proposedDir
                    self.move(self)
            self.restoreCheckbox(checkbox)
