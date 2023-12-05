import pygame
from entity import Entity
from globalValues import *


class Pacman(Entity):
    def __init__(self, width, height, posX, posY, isCheckbox=True):
        super().__init__(width, height, posX, posY)
        if isCheckbox == False:
            self.images = []
            for i in range(1, 5):
                self.images.append(
                    pygame.transform.scale(
                        pygame.image.load(f"assets/pacman_images/{i}.png"), (50, 50)
                    )
                )
            self.currentImageIdx = 0
            self.image = self.images[self.currentImageIdx]
            self.animationCounter = 0
        self.currentDir = Direction.RIGHT
        self.proposedDir = Direction.RIGHT
        self.FPSCounter = 0

    def createCheckbox(self):
        ret = Pacman(
            self.rect.width,
            self.rect.height,
            self.rect.centerx,
            self.rect.centery,
        )
        ret.currentDir, ret.proposedDir = self.currentDir, self.proposedDir
        return ret

    def checkMoveForward(self, checkbox, walls):
        self.move(checkbox)
        if not self.checkCollisionWithWalls(checkbox, walls):
            self.move(self)
            self.transferPosToOppositeSide()

    def update(self, walls):
        checkbox = self.createCheckbox()
        for _ in range(VELOCITY):
            if (self.FPSCounter % 5 == 0):
                if self.FPSCounter == 60:
                    self.FPSCounter = 0
                self.FPSCounter += 1
            else:
                if self.currentDir == self.proposedDir:
                    self.checkMoveForward(checkbox, walls)
                else:
                    checkbox.currentDir = checkbox.proposedDir
                    self.move(checkbox)
                    if self.checkCollisionWithWalls(checkbox, walls):
                        checkbox = self.createCheckbox()
                        self.checkMoveForward(checkbox, walls)
                    else:
                        self.currentDir = self.proposedDir
                        self.move(self)
                if self.FPSCounter == 60:
                    self.FPSCounter = 0
                self.FPSCounter += 1

    def draw(self, screen):
        match self.currentDir:
            case Direction.UP:
                screen.blit(
                    pygame.transform.rotate(self.images[self.currentImageIdx], 90),
                    (self.rect.centerx - 25, self.rect.centery - 25),
                )
            case Direction.DOWN:
                screen.blit(
                    pygame.transform.rotate(self.images[self.currentImageIdx], 270),
                    (self.rect.centerx - 25, self.rect.centery - 25),
                )
            case Direction.LEFT:
                screen.blit(
                    pygame.transform.flip(
                        self.images[self.currentImageIdx], True, False
                    ),
                    (self.rect.centerx - 25, self.rect.centery - 25),
                )
            case Direction.RIGHT:
                screen.blit(
                    self.images[self.currentImageIdx],
                    (self.rect.centerx - 25, self.rect.centery - 25),
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
