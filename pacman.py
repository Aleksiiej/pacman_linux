from globalValues import *

class Pacman:
    Colour = [255, 0, 0]
    x = 30
    y = 30
    width = 40
    height = 40

    def isMoveLeftPossible(self):
        if self.x > 0:
            return True
        else: return False

    def isMoveRightPossible(self):
        if self.x < SCREENSIZE[0] - self.width:
            return True
        else: return False
    
    def isMoveUpPossible(self):
        if self.y > 0:
            return True
        else: return False
    
    def isMoveDownPossible(self):
        if self.y < SCREENSIZE[1] - self.height:
            return True
        else: return False
        
    def moveLeft(self):
        if self.isMoveLeftPossible():
            self.x -= 5
    
    def moveRight(self):
        if self.isMoveRightPossible():
            self.x += 5
    
    def moveUp(self):
        if self.isMoveUpPossible():
            self.y -= 5

    def moveDown(self):
        if self.isMoveDownPossible():
            self.y += 5

    