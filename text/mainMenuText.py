import pygame
from globalValues import *


class MainMenuText:
    def __init__(self):
        self.text = pygame.font.SysFont(None, 24)
        self.message = [
            "1. Start Game",
            "2. Exit Program",
            "To navigate choose number",
            "on keyboard",
        ]
        self.mainMenuTextImages = []
        for line in self.message:
            self.mainMenuTextImages.append(self.text.render(line, True, RED))

    def draw(self, screen):
        posY = 50
        for line in self.mainMenuTextImages:
            screen.blit(line, (780, posY))
            posY += 30
