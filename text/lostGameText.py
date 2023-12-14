import pygame
from globalValues import *


class LostGameText:
    def __init__(self):
        self.text = pygame.font.SysFont(None, 24)
        self.message = ["You lose!"]
        self.lostGameTextImages = []
        for line in self.message:
            self.lostGameTextImages.append(self.text.render(line, True, RED))

    def updateScore(self, scoreCounter):
        self.message.append("You score is: " + str(scoreCounter.score))
        self.lostGameTextImages.append(self.text.render(self.message[1], True, RED))
        self.message.append("Press any key to proceed... ")
        self.lostGameTextImages.append(self.text.render(self.message[2], True, RED))

    def draw(self, screen):
        posY = 50
        for line in self.lostGameTextImages:
            screen.blit(line, (780, posY))
            posY += 30
