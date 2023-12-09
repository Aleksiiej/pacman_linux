import pygame
from globalValues import *


class WonGameText:
    def __init__(self):
        self.text = pygame.font.SysFont(None, 24)
        self.message = [
            "You won!"
        ]
        self.startgameTextImages = []
        for line in self.message:
            self.startgameTextImages.append(self.text.render(line, True, RED))

    def updateScore(self, scoreCounter):
        self.message.append("You score is: " + scoreCounter.score)

    def draw(self, screen):
        posY = 50
        for line in self.startgameTextImages:
            screen.blit(line, (780, posY))
            posY += 30
