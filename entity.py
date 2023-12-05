import pygame
from globalValues import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]

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

    def checkCollisionWithWalls(self, checkbox, walls):
        for wall in walls:
            if checkbox.rect.colliderect(wall):
                return True
        return False

    def transferPosToOppositeSide(self):
        if self.rect.centerx < 0:
            self.rect.centerx = 760
        if self.rect.centerx > 760:
            self.rect.centerx = 0
