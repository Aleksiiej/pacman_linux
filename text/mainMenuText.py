import pygame
from globalValues import *


class MainMenuText:
    def __init__(self):
        self.text_ = pygame.font.SysFont(None, 24)
        self.message_ = [
            "1. Start Game",
            "2. Exit Program",
            "To navigate choose number",
            "on keyboard",
        ]
        self.mainMenuTextImages_= []
        for line in self.message_:
            self.mainMenuTextImages_.append(self.text_.render(line, True, RED))

    def draw(self, screen):
        posY = 50
        for line in self.mainMenuTextImages_:
            screen.blit(line, (780, posY))
            posY += 30
