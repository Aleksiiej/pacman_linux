import pygame
import sys
from globalValues import *
from entities.pacman import Pacman
from entities.blinky import Blinky
from text.scoreCounter import ScoreCounter
from text.startgameText import StartgameText
from text.wonGameText import WonGameText
from text.lostGameText import LostGameText
from text.mainMenuText import MainMenuText
from map.map import prepareMap


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        self.mainMenuText = MainMenuText()
        self.initNewGame()

    def processInput(self):
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
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
                        pygame.quit()
                        sys.exit()

    def update(self):
        self.pacman.update(self.wallGroup)
        self.blinky.update(self.wallGroup, self.pacman)
        self.running = not self.checkIfLost()
        if not self.running:
            self.gameResult = False
        for apple in self.appleGroup:
            if apple.rect.colliderect(self.pacman):
                self.appleGroup.remove(apple)
                if len(self.appleGroup) == 0:
                    self.running = False
                    self.gameResult = True
                    break
                self.scoreCounter.incrementScore()
                break

    def render(self):
        self.screen.fill(BLACK)
        self.pacman.draw(self.screen)
        self.wallGroup.draw(self.screen)
        self.appleGroup.draw(self.screen)
        self.blinky.draw(self.screen)
        self.scoreCounter.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while True:
            self.render()
            self.mainMenuText.draw(self.screen)
            pygame.display.flip()
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                while True:
                    self.render()
                    self.startgameText.draw(self.screen)
                    pygame.display.flip()
                    pygame.event.clear()
                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        while self.running:
                            self.processInput()
                            self.update()
                            self.render()
                            self.clock.tick(FPS)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    else:
                        pass
                    if not self.running:
                        self.running = True
                        self.initNewGame()
                        break

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                pygame.quit()
                sys.exit()
            else:
                pass

    def checkIfLost(self):
        for ghost in self.ghostGroup:
            if ghost.calculateDistance(self.pacman, ghost) < 20:
                return True
            return False

    def initNewGame(self):
        self.pacman = Pacman(
            ENTITY_SIZE, ENTITY_SIZE, PACMAN_START_X, PACMAN_START_Y, False
        )
        self.blinky = Blinky(
            ENTITY_SIZE, ENTITY_SIZE, BLINKY_START_X, BLINKY_START_Y, False
        )
        self.ghostGroup = pygame.sprite.Group()
        self.ghostGroup.add(self.blinky)
        self.wallGroup = pygame.sprite.Group()
        self.appleGroup = pygame.sprite.Group()
        prepareMap(self.wallGroup, self.appleGroup)

        self.startgameText = StartgameText()
        self.scoreCounter = ScoreCounter()
        self.wonGameText = WonGameText()
        self.lostGameText = LostGameText()
        self.running = True
        self.gameResult = False
