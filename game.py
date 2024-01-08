import pygame
import sys
from globalValues import *
from entities.pacman import Pacman
from entities.blinky import Blinky
from entities.pinky import Pinky
from text.scoreCounter import ScoreCounter
from text.startgameText import StartgameText
from text.wonGameText import WonGameText
from text.lostGameText import LostGameText
from text.mainMenuText import MainMenuText
from map.map import prepareMap
from map.wall import Wall
from math import hypot
from asyncScatterTimer import AsyncScatterTimer
from asyncFrightenedTimer import AsyncFrightenedTimer


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption("Pacman")
        self.clock = pygame.time.Clock()
        self.mainMenuText = MainMenuText()
        self.initNewGame()

    def initNewGame(self):
        self.pacman = Pacman(
            ENTITY_SIZE, ENTITY_SIZE, PACMAN_START_X, PACMAN_START_Y, False
        )
        self.ghostGroup = pygame.sprite.Group()
        self.ghostGroup.add(
            Blinky(ENTITY_SIZE, ENTITY_SIZE, BLINKY_START_X, BLINKY_START_Y, False)
        )
        self.ghostGroup.add(
            Pinky(ENTITY_SIZE, ENTITY_SIZE, PINKY_START_X, PINKY_START_Y, False)
        )
        self.wallGroup = pygame.sprite.Group()
        self.gateGroup = pygame.sprite.Group()
        self.appleGroup = pygame.sprite.Group()
        self.powerUpGroup = pygame.sprite.Group()
        prepareMap(self.wallGroup, self.appleGroup, self.powerUpGroup)

        self.startgameText = StartgameText()
        self.scoreCounter = ScoreCounter()
        self.wonGameText = WonGameText()
        self.lostGameText = LostGameText()
        self.running = True
        self.gameResult = False
        self.wasBoxClosed = False

    def run(self):
        while True:
            self.showMainMenuText()

            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                while True:
                    self.showStartGameText()

                    event = pygame.event.wait()
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        asyncScatterTimer = AsyncScatterTimer(self)
                        asyncScatterTimer.start()
                        asyncFrightenedTimer = AsyncFrightenedTimer(self)
                        asyncFrightenedTimer.start()
                        self.gameLoop(asyncScatterTimer, asyncFrightenedTimer)
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    else:
                        pass

                    if not self.running:
                        asyncScatterTimer.join()
                        self.showEndgameText()
                        pygame.event.wait()
                        self.initNewGame()
                        break

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                pygame.quit()
                sys.exit()
            else:
                pass

    def gameLoop(self, asyncScatterTimer, asyncFrightenedTimer):
        while self.running:
            self.processInput(asyncScatterTimer, asyncFrightenedTimer)
            self.update(asyncScatterTimer, asyncFrightenedTimer)
            self.render()
            self.clock.tick(FPS)

    def processInput(self, asyncScatterTimer, asyncFrightenedTimer):
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
                        asyncScatterTimer.join()
                        asyncFrightenedTimer.join()
                        pygame.quit()
                        sys.exit()

    def update(self, asyncScatterTimer, asyncFrightenedTimer):
        self.handleGate()
        self.handleTimers(asyncScatterTimer, asyncFrightenedTimer)
        self.pacman.update(self.wallGroup)
        self.ghostGroup.update(self.wallGroup, self.pacman)
        self.running = not self.handleGhostCollision(self.pacman, asyncFrightenedTimer)
        if not self.running:
            self.gameResult = False
        self.handlePowerUpCollision(asyncFrightenedTimer)
        self.handleAppleCollision()

    def handleGate(self):
        counter = 0
        for ghost in self.ghostGroup:
            if (
                not ghost.ghostState == GhostStates.InBox
                and not ghost.ghostState == GhostStates.Eaten
            ):
                counter += 1
        if counter == len(self.ghostGroup) and not self.wasBoxClosed:
            self.gateGroup.add(
                Wall(
                    ENTITY_SIZE,
                    ENTITY_SIZE,
                    380,
                    340,
                    BLUE,
                )
            )
            self.wasBoxClosed = True
        else:
            self.gateGroup.remove()

    def handleTimers(self, asyncScatterTimer, asyncFrightenedTimer):
        if (
            asyncScatterTimer.currentTime > 20
            and self.ghostGroup.sprites()[0].ghostState == GhostStates.Chase
        ):
            asyncScatterTimer.currentTime = 0
            for ghost in self.ghostGroup:
                ghost.ghostState = GhostStates.Scatter
        elif (
            asyncScatterTimer.currentTime > 7
            and self.ghostGroup.sprites()[0].ghostState == GhostStates.Scatter
        ):
            asyncScatterTimer.currentTime = 0
            for ghost in self.ghostGroup:
                ghost.ghostState = GhostStates.Chase

        if (
            asyncFrightenedTimer.currentTime > 12
            and self.ghostGroup.sprites()[0].ghostState == GhostStates.Frightened
        ):
            asyncFrightenedTimer.currentTime = 0
            for ghost in self.ghostGroup:
                ghost.ghostState = GhostStates.Chase

    def handleGhostCollision(self, pacman, asyncFrightenedTimer):
        for ghost in self.ghostGroup:
            if (
                hypot(
                    pacman.rect.centerx - ghost.rect.centerx,
                    pacman.rect.centery - ghost.rect.centery,
                )
                < 20
            ):
                if (
                    ghost.ghostState == GhostStates.Chase
                    or ghost.ghostState == GhostStates.Scatter
                    or ghost.ghostState == GhostStates.InBox
                ):
                    return True
                else:
                    asyncFrightenedTimer.currentTime = 0
                    if ghost.ghostState == GhostStates.Frightened:
                        self.scoreCounter.incrementScoreBy30()
                        # for ghost in self.ghostGroup:
                        ghost.ghostState = GhostStates.Eaten
                    return False

    def handlePowerUpCollision(self, asyncFrightenedTimer):
        for powerUp in self.powerUpGroup:
            if powerUp.rect.colliderect(self.pacman):
                for ghost in self.ghostGroup:
                    ghost.ghostState = GhostStates.Frightened
                    ghost.reverseDir()
                asyncFrightenedTimer.currentTime = 0
                self.scoreCounter.incrementScoreBy5()
                self.powerUpGroup.remove(powerUp)
                if len(self.powerUpGroup) == 0:
                    del self.powerUpGroup
                pass

    def handleAppleCollision(self):
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
        self.gateGroup.draw(self.screen)
        if len(self.appleGroup) > 0:
            self.appleGroup.draw(self.screen)
        if len(self.powerUpGroup) > 0:
            self.powerUpGroup.draw(self.screen)
        for ghost in self.ghostGroup:
            ghost.draw(self.screen)
        self.scoreCounter.draw(self.screen)
        pygame.display.flip()

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
