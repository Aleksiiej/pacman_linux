import pygame
from globalValues import *


class StartgameText:
    def __init__(self):
        self.text = pygame.font.SysFont(None, 24)
        self.message = [
            "Welcome in Pacman",
            "INSTRUCTIONS:",
            "ARROW KEYS to control Pacman",
            "P to pause and unpause game",
            "Click ENTER to start game",
        ]
        self.startgameTextImages = []
        for line in self.message:
            self.startgameTextImages.append(self.text.render(line, True, RED))

    def draw(self, screen):
        posY = 50
        for line in self.startgameTextImages:
            screen.blit(line, (970, posY))
            posY += 30
