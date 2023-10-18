import pygame
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
        self.currentDir = Direction.RIGHT
        self.proposedDir = Direction.RIGHT

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
