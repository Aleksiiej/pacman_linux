from globalValues import *
import pygame

class Pacman(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
       pygame.sprite.Sprite.__init__(self)

       self.image = pygame.Surface([width, height])
       self.image.fill(color)

       self.rect = self.image.get_rect()

       self.currentDir = Direction.RIGHT
    
    velocity = 4

    def isMoveLeftPossible(self):
        if self.rect.x > 0:
            return True
        else: return False

    def isMoveRightPossible(self):
        if self.rect.x < SCREENSIZE[0] - self.rect.width:
            return True
        else: return False
    
    def isMoveUpPossible(self):
        if self.rect.y > 0:
            return True
        else: return False
    
    def isMoveDownPossible(self):
        if self.rect.y < SCREENSIZE[1] - self.rect.height:
            return True
        else: return False
        
    def changeDirToLeft(self):
        if self.isMoveLeftPossible():
            self.currentDir = Direction.LEFT
    
    def changeDirToRight(self):
        if self.isMoveRightPossible():
            self.currentDir = Direction.RIGHT
    
    def changeDirToUp(self):
        if self.isMoveUpPossible():
            self.currentDir = Direction.UP

    def changeDirToDown(self):
        if self.isMoveDownPossible():
            self.currentDir = Direction.DOWN

    def move(self):
        match self.currentDir:
            case Direction.LEFT:
                if self.isMoveLeftPossible():
                    self.rect.x -= self.velocity
            case Direction.RIGHT:
                if self.isMoveRightPossible():
                    self.rect.x += self.velocity
            case Direction.UP:
                if self.isMoveUpPossible():
                    self.rect.y -= self.velocity
            case Direction.DOWN:
                if self.isMoveDownPossible():
                    self.rect.y += self.velocity