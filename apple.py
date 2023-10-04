import pygame
from globalValues import *


class Apple(pygame.sprite.Sprite):
    image = pygame.transform.scale(
        pygame.image.load("assets/dot_images/apple.png"), (20, 20)
    )

    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.rect = Apple.image.get_rect()
        self.rect.center = [posX, posY]

    def draw(self, screen):
        screen.blit(Apple.image, (self.rect.x, self.rect.y))
