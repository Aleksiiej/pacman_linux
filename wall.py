from globalValues import *
import pygame


class Wall(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #    self.image = pygame.image.load("./content/image_file.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
