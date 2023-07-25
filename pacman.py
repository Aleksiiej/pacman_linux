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

    def checkCollisionWithWalls(self, checkbox, walls):
        for wall in walls:
            isCollision = checkbox.rect.colliderect(wall)
            if isCollision == True:
                return True
        return False

    def update(self, walls):
        for _ in range(VELOCITY):
            if self.currentDir == self.proposedDir:
                checkbox = self.createCheckbox()
                self.move(checkbox)
                isCollision = self.checkCollisionWithWalls(checkbox, walls)
                if isCollision:
                    pass
                else:
                    self.move(self)
            else:
                checkbox = self.createCheckbox()
                checkbox.currentDir = checkbox.proposedDir
                self.move(checkbox)
                isCollision = self.checkCollisionWithWalls(checkbox, walls)
                if isCollision:
                    checkbox.currentDir = self.currentDir
                    self.move(self)
                else:
                    self.currentDir = self.proposedDir
                    self.move(self)
