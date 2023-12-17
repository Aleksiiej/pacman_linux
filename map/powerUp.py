import pygame
from globalValues import *


class PowerUp(pygame.sprite.Sprite):
    image = pygame.transform.scale(
        pygame.image.load("assets/powerup_images/pear.png"), (POWERUP_SIZE, POWERUP_SIZE)
    )

    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)
        self.rect = PowerUp.image.get_rect()
        self.rect.center = [posX, posY]

    def draw(self, screen):
        screen.blit(PowerUp.image, (self.rect.x, self.rect.y))
