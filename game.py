import pygame
from globalValues import *
from pacman import Pacman
from blinky import Blinky
from scoreCounter import ScoreCounter
from startgameText import StartgameText
from map import prepareMap


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()

        self.pacman = Pacman(50, 50, 75, 75, False)
        self.blinky = Blinky(50, 50, 475, 400, False)
        self.ghostGroup = pygame.sprite.Group()
        self.ghostGroup.add(self.blinky)
        self.wallGroup = pygame.sprite.Group()
        self.appleGroup = pygame.sprite.Group()
        prepareMap(self.wallGroup, self.appleGroup)

        self.startgameText = StartgameText()

        self.running = True

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        self.pacman.proposedDir = Direction.UP
                    case pygame.K_DOWN:
                        self.pacman.proposedDir = Direction.DOWN
                    case pygame.K_LEFT:
                        self.pacman.proposedDir = Direction.LEFT
                    case pygame.K_RIGHT:
                        self.pacman.proposedDir = Direction.RIGHT
                    case pygame.K_ESCAPE:
                        self.running = False

    def update(self):
        self.pacman.update(self.wallGroup)
        self.blinky.update(self.wallGroup, self.pacman)
        for apple in self.appleGroup:
            if apple.rect.colliderect(self.pacman):
                self.appleGroup.remove(apple)
                if len(self.appleGroup) == 0:
                    self.running = False
                ScoreCounter.incrementScore()
                break
        for ghost in self.ghostGroup:
            if ghost.rect.colliderect(self.pacman):
                self.running = False

    def render(self):
        self.screen.fill(BLACK)
        self.pacman.draw(self.screen)
        self.wallGroup.draw(self.screen)
        self.appleGroup.draw(self.screen)
        self.blinky.draw(self.screen)
        self.startgameText.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(FPS)
