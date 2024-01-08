import pygame
from globalValues import *


class StartgameText:
    def __init__(self):
        self.text_ = pygame.font.SysFont(None, 24)
        self.message_ = [
            "Welcome in Pacman",
            "INSTRUCTIONS:",
            "ARROW KEYS to control Pacman",
            "P to pause and unpause game",
            "Press ENTER to start game...",
            "Or ESCAPE to exit game",
        ]
        self.startgameTextImages = []
        for line in self.message_:
            self.startgameTextImages.append(self.text_.render(line, True, RED))

    def draw(self, screen):
        posY = 50
        for line in self.startgameTextImages:
            screen.blit(line, (780, posY))
            posY += 30
