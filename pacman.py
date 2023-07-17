from entity import Entity
from globalValues import *


class Pacman(Entity):
    def __init__(self, width, height, posX, posY, color):
        super().__init__(width, height, posX, posY, color)

    def changeDir(self, newDir):
        self.currentDir = newDir

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
        return Pacman(
            self.image.get_width(),
            self.image.get_height(),
            self.rect.centerx,
            self.rect.centery,
            BLACK,
        )

    def update(self, walls):
        checkbox = self.createCheckbox()
        checkbox.currentDir = self.currentDir

        for _ in range(VELOCITY):
            self.move(checkbox)
            isCollision = False
            for wall in walls:
                isCollision = checkbox.rect.colliderect(wall)
                if isCollision == True:
                    break
            if isCollision == False:
                self.move(self)
            else:
                break
