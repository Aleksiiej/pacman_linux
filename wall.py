import pygame
from globalValues import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
