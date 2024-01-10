import pygame
from entities.entity import Entity
from globalValues import *


class Pacman(Entity):
    def __init__(self, width, height, posX, posY, refToGhostGroup, isCheckbox=True):
        super().__init__(width, height, posX, posY)
        if isCheckbox == False:
            self.images_ = [
                pygame.transform.scale(
                    pygame.image.load(f"assets/pacman_images/{i}.png"),
                    (ENTITY_SIZE, ENTITY_SIZE),
                )
                for i in range(1, 5)
            ]
            self.currentImageIdx_ = 0
            self.image_ = self.images_[self.currentImageIdx_]
            self.animationCounter = 0
        self.proposedDir_ = Direction.RIGHT
        self.FPSCounter_ = 0
        self.refToGhostGroup_ = refToGhostGroup

    def createCheckbox(self):
        ret = Pacman(
            self.rect.width,
            self.rect.height,
            self.rect.centerx,
            self.rect.centery,
            self.refToGhostGroup_,
        )
        ret.currentDir_, ret.proposedDir_ = self.currentDir_, self.proposedDir_
        return ret

    def checkMoveForward(self, checkbox, walls):
        self.move(checkbox)
        if not self.checkCollisionWithWalls(checkbox, walls):
            self.move(self)
            self.transferPosToOppositeSide()

    def update(self, walls):
        checkbox = self.createCheckbox()
        isAnyGhostFrightened = False
        PACMAN_VELOCITY = 0
        for ghost in self.refToGhostGroup_:
            if ghost.ghostState_ == GhostStates.Frightened:
                isAnyGhostFrightened = True
        if isAnyGhostFrightened:
            PACMAN_VELOCITY = 4
        else:
            PACMAN_VELOCITY = 3

        for _ in range(PACMAN_VELOCITY):
            if self.FPSCounter_ % 5 == 0:
                self.updateFPSCounter()
            else:
                if self.currentDir_ == self.proposedDir_:
                    self.checkMoveForward(checkbox, walls)
                else:
                    checkbox.currentDir_ = checkbox.proposedDir_
                    self.move(checkbox)
                    if self.checkCollisionWithWalls(checkbox, walls):
                        checkbox = self.createCheckbox()
                        self.checkMoveForward(checkbox, walls)
                    else:
                        self.currentDir_ = self.proposedDir_
                        self.move(self)
                self.updateFPSCounter()



    def updateFPSCounter(self):
        if self.FPSCounter_ == 60:
            self.FPSCounter_ = 0
        self.FPSCounter_ += 1

    def draw(self, screen):
        match self.currentDir_:
            case Direction.UP:
                screen.blit(
                    pygame.transform.rotate(self.images_[self.currentImageIdx_], 90),
                    (self.rect.centerx - 20, self.rect.centery - 20),
                )
            case Direction.DOWN:
                screen.blit(
                    pygame.transform.rotate(self.images_[self.currentImageIdx_], 270),
                    (self.rect.centerx - 20, self.rect.centery - 20),
                )
            case Direction.LEFT:
                screen.blit(
                    pygame.transform.flip(
                        self.images_[self.currentImageIdx_], True, False
                    ),
                    (self.rect.centerx - 20, self.rect.centery - 20),
                )
            case Direction.RIGHT:
                screen.blit(
                    self.images_[self.currentImageIdx_],
                    (self.rect.centerx - 20, self.rect.centery - 20),
                )

        self.animationCounter += 1

        match self.animationCounter:
            case 0:
                self.currentImageIdx_ = 0
            case 7:
                self.currentImageIdx_ = 1
            case 14:
                self.currentImageIdx_ = 2
            case 21:
                self.currentImageIdx_ = 3
                self.animationCounter = 0
