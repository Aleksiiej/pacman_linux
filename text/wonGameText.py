import pygame
from globalValues import *


class WonGameText:
    def __init__(self):
        self.text_ = pygame.font.SysFont(None, 24)
        self.message_ = ["You won!"]
        self.wonGameTextImages_ = []
        for line in self.message_:
            self.wonGameTextImages_.append(self.text_.render(line, True, RED))

    def updateScore(self, scoreCounter):
        self.message_.append("You score is: " + str(scoreCounter.score_))
        self.wonGameTextImages_.append(self.text_.render(self.message_[1], True, RED))
        self.message_.append("Press any key to proceed... ")
        self.wonGameTextImages_.append(self.text_.render(self.message_[2], True, RED))

    def draw(self, screen):
        posY = 50
        for line in self.wonGameTextImages_:
            screen.blit(line, (780, posY))
            posY += 30
