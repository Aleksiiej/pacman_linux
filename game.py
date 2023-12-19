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

    def run(self):
        while True:
            self.showMainMenuText()

            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                while True:
                    self.showStartGameText()

                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.gameLoop()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    else:
                        pass

                    if not self.running:
                        self.showEndgameText()
                        pygame.event.wait()
                        self.initNewGame()
                        break

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                pygame.quit()
                sys.exit()
            else:
                pass

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
        self.scatterTime = pygame.time.get_ticks() + self.scatterTime
        print(self.scatterTime)

        if self.scatterTime > 20000000 and self.blinky.ghostState == GhostStates.Chase:
            self.scatterTime = 0 
            self.blinky.ghostState = GhostStates.Scatter
        elif self.scatterTime > 7000000 and self.blinky.ghostState == GhostStates.Scatter:
            self.scatterTime = 0 
            self.blinky.ghostState = GhostStates.Chase

        self.pacman.update(self.wallGroup)
        self.blinky.update(self.wallGroup, self.pacman)
        self.running = not self.checkIfLost()
        if not self.running:
            self.gameResult = False

        for powerUp in self.powerUpGroup:
            if powerUp.rect.colliderect(self.pacman):
                # TODO: implemented changes for state machine
                # self.blinky.ghostState = GhostStates.Frightened
                self.scoreCounter.incrementScoreBy5()
                self.powerUpGroup.remove(powerUp)
                if len(self.powerUpGroup) == 0:
                    del self.powerUpGroup
                pass

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
        self.powerUpGroup.draw(self.screen)
        self.blinky.draw(self.screen)
        self.scoreCounter.draw(self.screen)
        pygame.display.flip()

    def gameLoop(self):
        while self.running:
            self.processInput()
            self.update()
            self.render()
            self.clock.tick(FPS)

    def checkIfLost(self):
        for ghost in self.ghostGroup:
            if (
                ghost.calculateDistance(self.pacman, ghost) < 20
                and ghost.ghostState != GhostStates.Frightened
            ):
                return True
            return False

    def showMainMenuText(self):
        self.render()
        self.mainMenuText.draw(self.screen)
        pygame.display.flip()

    def showStartGameText(self):
        self.render()
        self.startgameText.draw(self.screen)
        pygame.display.flip()

    def showEndgameText(self):
        if self.gameResult:
            self.wonGameText.updateScore(self.scoreCounter)
            self.wonGameText.draw(self.screen)
        else:
            self.lostGameText.updateScore(self.scoreCounter)
            self.lostGameText.draw(self.screen)
        pygame.display.flip()

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
        self.powerUpGroup = pygame.sprite.Group()
        prepareMap(self.wallGroup, self.appleGroup, self.powerUpGroup)

        self.startgameText = StartgameText()
        self.scoreCounter = ScoreCounter()
        self.wonGameText = WonGameText()
        self.lostGameText = LostGameText()
        self.running = True
        self.gameResult = False

        self.chaseTimer = pygame.time.Clock()
        self.scatterTimer = pygame.time.Clock()
        self.scatterTime = 0
