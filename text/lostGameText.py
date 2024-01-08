import pygame
from globalValues import *


class LostGameText:
    def __init__(self):
        self.text_ = pygame.font.SysFont(None, 24)
        self.message_ = ["You lose!"]
        self.lostGameTextImages_ = []
        for line in self.message_:
            self.lostGameTextImages_.append(self.text_.render(line, True, RED))

    def updateScore(self, scoreCounter):
        self.message_.append("You score is: " + str(scoreCounter.score))
        self.lostGameTextImages_.append(self.text_.render(self.message_[1], True, RED))
        self.message_.append("Press any key to proceed... ")
        self.lostGameTextImages_.append(self.text_.render(self.message_[2], True, RED))

    def draw(self, screen):
        posY = 50
        for line in self.lostGameTextImages_:
            screen.blit(line, (780, posY))
            posY += 30
