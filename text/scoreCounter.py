import pygame
from globalValues import *


class ScoreCounter:
    def __init__(self):
        self.score = 0
        self.text = pygame.font.SysFont(None, 36)
        self.textImg = self.text.render("Score: " + str(self.score), True, RED)

    def incrementScore(self):
        self.score += 1
        self.textImg = self.text.render("Score: " + str(self.score), True, RED)
    
    def incrementScoreBy5(self):
        self.score += 5
        self.textImg = self.text.render("Score: " + str(self.score), True, RED)

    def draw(self, screen):
        screen.blit(self.textImg, (780, 400))
