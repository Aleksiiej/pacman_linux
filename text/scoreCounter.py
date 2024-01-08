import pygame
from globalValues import *


class ScoreCounter:
    def __init__(self):
        self.score_ = 0
        self.text_ = pygame.font.SysFont(None, 36)
        self.textImg_ = self.text_.render("Score: " + str(self.score_), True, RED)

    def incrementScore(self):
        self.score_ += 1
        self.textImg_ = self.text_.render("Score: " + str(self.score_), True, RED)
    
    def incrementScoreBy5(self):
        self.score_ += 5
        self.textImg_ = self.text_.render("Score: " + str(self.score_), True, RED)

    def incrementScoreBy30(self):
        self.score_ += 30
        self.textImg_ = self.text_.render("Score: " + str(self.score_), True, RED)

    def draw(self, screen):
        screen.blit(self.textImg_, (780, 400))
