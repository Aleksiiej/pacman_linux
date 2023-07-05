from globalValues import *

class Pacman:
    Colour = [255, 0, 0]
    x = 30
    y = 30
    width = 40
    height = 40
    velocity = 5
    currentDir = Direction.RIGHT

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

    def move(self, dt):
        match self.currentDir:
            case Direction.LEFT:
                if self.isMoveLeftPossible():
                    self.x -= self.velocity * dt
            case Direction.RIGHT:
                if self.isMoveRightPossible():
                    self.x += self.velocity * dt
            case Direction.UP:
                if self.isMoveUpPossible():
                    self.y -= self.velocity * dt
            case Direction.DOWN:
                if self.isMoveDownPossible():
                    self.y += self.velocity * dt