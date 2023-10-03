import pygame
from globalValues import *


class Apple(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, color=YELLOW):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/dot_images/apple.png"), (20, 20)
        )
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]

    def update(self, screen):
            screen.blit(
                self.image,
                (self.rect.centerx - 10, self.rect.centery - 10),
            )
