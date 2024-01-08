import pygame
from entities.entity import Entity
from globalValues import *


class Pacman(Entity):
    def __init__(self, width, height, posX, posY, isCheckbox=True):
        super().__init__(width, height, posX, posY)
        if isCheckbox == False:
            self.images = [
                pygame.transform.scale(
                    pygame.image.load(f"assets/pacman_images/{i}.png"),
                    (ENTITY_SIZE, ENTITY_SIZE),
                )
                for i in range(1, 5)
            ]
            self.currentImageIdx = 0
            self.image = self.images[self.currentImageIdx]
            self.animationCounter = 0
        self.proposedDir = Direction.RIGHT
        self.FPSCounter = 0

    def createCheckbox(self):
        ret = Pacman(
            self.rect.width,
            self.rect.height,
            self.rect.centerx,
            self.rect.centery,
        )
        ret.currentDir_, ret.proposedDir = self.currentDir_, self.proposedDir
        return ret

    def checkMoveForward(self, checkbox, walls):
        self.move(checkbox)
        if not self.checkCollisionWithWalls(checkbox, walls):
            self.move(self)
            self.transferPosToOppositeSide()

    def update(self, walls):
        checkbox = self.createCheckbox()
        for _ in range(VELOCITY):
            if self.FPSCounter % 5 == 0:
                self.updateFPSCounter()
            else:
                if self.currentDir_ == self.proposedDir:
                    self.checkMoveForward(checkbox, walls)
                else:
                    checkbox.currentDir_ = checkbox.proposedDir
                    self.move(checkbox)
                    if self.checkCollisionWithWalls(checkbox, walls):
                        checkbox = self.createCheckbox()
                        self.checkMoveForward(checkbox, walls)
                    else:
                        self.currentDir_ = self.proposedDir
                        self.move(self)
                self.updateFPSCounter()

    def updateFPSCounter(self):
        if self.FPSCounter == 60:
            self.FPSCounter = 0
        self.FPSCounter += 1

    def draw(self, screen):
        match self.currentDir_:
            case Direction.UP:
                screen.blit(
                    pygame.transform.rotate(self.images[self.currentImageIdx], 90),
                    (self.rect.centerx - 20, self.rect.centery - 20),
                )
            case Direction.DOWN:
                screen.blit(
                    pygame.transform.rotate(self.images[self.currentImageIdx], 270),
                    (self.rect.centerx - 20, self.rect.centery - 20),
                )
            case Direction.LEFT:
                screen.blit(
                    pygame.transform.flip(
                        self.images[self.currentImageIdx], True, False
                    ),
                    (self.rect.centerx - 20, self.rect.centery - 20),
                )
            case Direction.RIGHT:
                screen.blit(
                    self.images[self.currentImageIdx],
                    (self.rect.centerx - 20, self.rect.centery - 20),
                )

        self.animationCounter += 1

        match self.animationCounter:
            case 0:
                self.currentImageIdx = 0
            case 7:
                self.currentImageIdx = 1
            case 14:
                self.currentImageIdx = 2
            case 21:
                self.currentImageIdx = 3
                self.animationCounter = 0
