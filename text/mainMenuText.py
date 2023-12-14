import pygame
from globalValues import *


class MainMenuText:
    def __init__(self):
        self.text = pygame.font.SysFont(None, 24)
        self.message = [
            "1. Start Game",
            "2. Exit Program",
        ]
        self.startgameTextImages = []
        for line in self.message:
            self.startgameTextImages.append(self.text.render(line, True, RED))

    def draw(self, screen):
        posY = 50
        for line in self.startgameTextImages:
            screen.blit(line, (780, posY))
            posY += 30