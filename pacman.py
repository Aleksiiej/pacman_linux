from globalValues import *
import pygame


class Pacman(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        #    self.image = pygame.image.load("./content/image_file.png")
        self.rect = self.image.get_rect()
        self.rect.center = [posX, posY]
        self.currentDir = Direction.RIGHT
        self.prevousDir = Direction.RIGHT
    velocity = 4
    
    def changeDirToLeft(self):
        self.prevousDir = self.currentDir
        self.currentDir = Direction.LEFT

    def changeDirToRight(self):
        self.prevousDir = self.currentDir
        self.currentDir = Direction.RIGHT

    def changeDirToUp(self):
        self.prevousDir = self.currentDir
        self.currentDir = Direction.UP

    def changeDirToDown(self):
        self.prevousDir = self.currentDir
        self.currentDir = Direction.DOWN

    def update(self, walls):
        isCollision = False
        for wall in walls:
            isCollision = self.rect.colliderect(wall)
            if isCollision == True:
                break
        if isCollision == False:
            match self.currentDir:
                case Direction.LEFT:
                    self.rect.x -= self.velocity
                case Direction.RIGHT:
                    self.rect.x += self.velocity
                case Direction.UP:
                    self.rect.y -= self.velocity
                case Direction.DOWN:
                    self.rect.y += self.velocity
