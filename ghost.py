import pygame
from math import hypot
from globalValues import *


class Ghost(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, isCheckbox=True):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
        if isCheckbox == False:
            self.image = pygame.transform.scale(
                pygame.image.load(f"assets/ghost_images/blue.png"), (50, 50)
            )
        self.currentDir = Direction.LEFT
        self.restrictedDir = Direction.RIGHT
        self.ghostState = GhostStates.InBox

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
        ret = Ghost(
            self.rect.width,
            self.rect.height,
            self.rect.centerx,
            self.rect.centery,
        )
        return ret

    def checkCollisionWithWalls(self, checkbox, walls):
        for wall in walls:
            if checkbox.rect.colliderect(wall):
                return True
        return False

    def calculateDistance(self, pacman, checkbox) -> float:
        return hypot(
            pacman.rect.centerx - checkbox.rect.centerx,
            pacman.rect.centery - checkbox.rect.centerx,
        )

    def update(self, walls, pacman):
        checkbox = self.createCheckbox()

        for _ in range(VELOCITY):
            possibleDirections = {}
            print(self.currentDir)
            for dir in DIRECTION_LIST:
                checkbox = self.createCheckbox()
                checkbox.currentDir = dir
                self.moveCheckbox(checkbox)
                if not checkbox.checkCollisionWithWalls(checkbox, walls):
                    possibleDirections[dir] = self.calculateDistance(pacman, checkbox)

            if self.restrictedDir in possibleDirections:
                del possibleDirections[self.restrictedDir]

            print(possibleDirections)
            if self.ghostState == GhostStates.InBox and len(possibleDirections) == 2:
                self.currentDir = Direction.UP
                self.restrictedDir = Direction.DOWN
                self.ghostState = GhostStates.Chasing
            elif len(possibleDirections) > 0:
                self.currentDir = min(possibleDirections, key=possibleDirections.get)

            match self.currentDir:
                case Direction.UP:
                    self.restrictedDir = Direction.DOWN
                case Direction.DOWN:
                    self.restrictedDir = Direction.UP
                case Direction.LEFT:
                    self.restrictedDir = Direction.RIGHT
                case Direction.RIGHT:
                    self.restrictedDir = Direction.LEFT

            self.move(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
