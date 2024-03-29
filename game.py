import pygame
import sys
from globalValues import *
from entities.pacman import Pacman
from entities.blinky import Blinky
from entities.pinky import Pinky
from entities.inky import Inky
from entities.clyde import Clyde
from text.scoreCounter import ScoreCounter
from text.startgameText import StartgameText
from text.wonGameText import WonGameText
from text.lostGameText import LostGameText
from text.mainMenuText import MainMenuText
from text.pauseText import PauseText
from map.wall import Wall
from timers.asyncScatterTimer import AsyncScatterTimer
from timers.asyncFrightenedTimer import AsyncFrightenedTimer
from map.map import prepareMap
from math import hypot


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen_ = pygame.display.set_mode(SCREENSIZE)
        pygame.display.set_caption("Pacman")
        self.clock_ = pygame.time.Clock()
        self.mainMenuText_ = MainMenuText()
        self.initNewGame()

    def initNewGame(self):
        self.ghostGroup_ = pygame.sprite.Group()
        self.ghostGroup_.add(
            Blinky(ENTITY_SIZE, ENTITY_SIZE, BLINKY_START_X, BLINKY_START_Y, False)
        )
        self.ghostGroup_.add(
            Pinky(ENTITY_SIZE, ENTITY_SIZE, PINKY_START_X, PINKY_START_Y, False)
        )
        self.ghostGroup_.add(
            Inky(ENTITY_SIZE, ENTITY_SIZE, INKY_START_X, INKY_START_Y, False)
        )
        self.ghostGroup_.add(
            Clyde(ENTITY_SIZE, ENTITY_SIZE, CLYDE_START_X, CLYDE_START_Y, False)
        )
        self.pacman_ = Pacman(
            ENTITY_SIZE,
            ENTITY_SIZE,
            PACMAN_START_X,
            PACMAN_START_Y,
            self.ghostGroup_,
            False,
        )
        self.wallGroup_ = pygame.sprite.Group()
        self.gateGroup_ = pygame.sprite.Group()
        self.appleGroup_ = pygame.sprite.Group()
        self.powerUpGroup_ = pygame.sprite.Group()
        prepareMap(self.wallGroup_, self.appleGroup_, self.powerUpGroup_)
        self.gateGroup_.add(
            Wall(
                ENTITY_SIZE,
                ENTITY_SIZE,
                380,
                340,
                BLUE,
            )
        )

        self.startgameText_ = StartgameText()
        self.scoreCounter_ = ScoreCounter()
        self.wonGameText_ = WonGameText()
        self.lostGameText_ = LostGameText()
        self.pauseText_ = PauseText()
        self.running_ = True
        self.gameResult_ = False
        self.wasBoxClosed_ = False
        self.appleCounter_ = 0
        self.releaseGhostCounter = 0

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

                    if not self.running_:
                        asyncScatterTimer.join()
                        asyncFrightenedTimer.join()
                        self.showEndgameText()
                        while True:
                            event = pygame.event.wait()
                            if event.type == pygame.KEYDOWN:
                                break
                        self.initNewGame()
                        break

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                pygame.quit()
                sys.exit()
            else:
                pass

    def gameLoop(self, asyncScatterTimer, asyncFrightenedTimer):
        while self.running_:
            self.processInput(asyncScatterTimer, asyncFrightenedTimer)
            self.update(asyncScatterTimer, asyncFrightenedTimer)
            self.render()
            self.clock_.tick(FPS)

    def processInput(self, asyncScatterTimer, asyncFrightenedTimer):
        for event in pygame.event.get():
            if (
                event.type == pygame.QUIT
                or event.type == pygame.KEYDOWN
                and event.key == pygame.K_ESCAPE
            ):
                self.running_ = False
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        self.pacman_.proposedDir_ = Direction.UP
                    case pygame.K_DOWN:
                        self.pacman_.proposedDir_ = Direction.DOWN
                    case pygame.K_LEFT:
                        self.pacman_.proposedDir_ = Direction.LEFT
                    case pygame.K_RIGHT:
                        self.pacman_.proposedDir_ = Direction.RIGHT
                    case pygame.K_ESCAPE:
                        self.showPauseText()
                        while True:
                            event = pygame.event.wait()
                            if event.type == pygame.KEYDOWN:
                                match event.key:
                                    case pygame.K_1:
                                        break
                                    case pygame.K_2:
                                        asyncScatterTimer.join()
                                        asyncFrightenedTimer.join()
                                        pygame.quit()
                                        sys.exit()

    def update(self, asyncScatterTimer, asyncFrightenedTimer):
        self.handleWaitingGhosts()
        self.handleTimers(asyncScatterTimer, asyncFrightenedTimer)
        self.pacman_.update(self.wallGroup_)
        self.ghostGroup_.update(self.wallGroup_, self.pacman_)
        self.running_ = not self.handleGhostCollision(self.pacman_)
        if not self.running_:
            self.gameResult_ = False
        self.handlePowerUpCollision(asyncFrightenedTimer)
        self.handleAppleCollision()

    def handleWaitingGhosts(self):
        if self.releaseGhostCounter < 2:
            if self.appleCounter_ == 30 and self.releaseGhostCounter == 0:
                self.releaseOneGhost()
            if self.appleCounter_ == 70 and self.releaseGhostCounter == 1:
                self.releaseOneGhost()

    def releaseOneGhost(self):
        for ghost in self.ghostGroup_:
            if ghost.ghostState_ == GhostStates.Wait:
                self.releaseGhostCounter += 1
                ghost.ghostState_ = GhostStates.Chase
                break

    def handleTimers(self, asyncScatterTimer, asyncFrightenedTimer):
        if asyncScatterTimer.currentTime_ > CHASE_TIME:
            asyncScatterTimer.resetTimer()
            for ghost in self.ghostGroup_:
                if ghost.ghostState_ == GhostStates.Chase:
                    ghost.ghostState_ = GhostStates.Scatter
        elif asyncScatterTimer.currentTime_ > SCATTER_TIME:
            asyncScatterTimer.resetTimer()
            for ghost in self.ghostGroup_:
                if ghost.ghostState_ == GhostStates.Scatter:
                    ghost.ghostState_ = GhostStates.Chase

        if asyncFrightenedTimer.currentTime_ > FRIGHTENED_TIME:
            asyncFrightenedTimer.resetTimer()
            for ghost in self.ghostGroup_:
                if ghost.ghostState_ == GhostStates.Frightened:
                    ghost.ghostState_ = GhostStates.Chase

    def handleGhostCollision(self, pacman_):
        for ghost in self.ghostGroup_:
            if (
                hypot(
                    pacman_.rect.centerx - ghost.rect.centerx,
                    pacman_.rect.centery - ghost.rect.centery,
                )
                < 20
            ):
                if (
                    ghost.ghostState_ == GhostStates.Chase
                    or ghost.ghostState_ == GhostStates.Scatter
                    or ghost.ghostState_ == GhostStates.InBox
                ):
                    return True
                else:
                    if ghost.ghostState_ == GhostStates.Frightened:
                        self.scoreCounter_.incrementScoreBy30()
                        ghost.ghostState_ = GhostStates.Eaten
                    return False

    def handlePowerUpCollision(self, asyncFrightenedTimer):
        for powerUp in self.powerUpGroup_:
            if powerUp.rect.colliderect(self.pacman_):
                for ghost in self.ghostGroup_:
                    if (
                        ghost.ghostState_ == GhostStates.Chase
                        or ghost.ghostState_ == GhostStates.Scatter
                    ):
                        ghost.ghostState_ = GhostStates.Frightened
                        ghost.reverseDir()
                asyncFrightenedTimer.currentTime_ = 0
                self.scoreCounter_.incrementScoreBy5()
                self.powerUpGroup_.remove(powerUp)

    def handleAppleCollision(self):
        for apple in self.appleGroup_:
            if apple.rect.colliderect(self.pacman_):
                self.appleGroup_.remove(apple)
                self.appleCounter_ += 1
                if len(self.appleGroup_) == 0:
                    self.running_ = False
                    self.gameResult_ = True
                    break
                self.scoreCounter_.incrementScore()
                break

    def render(self):
        self.screen_.fill(BLACK)
        self.pacman_.draw(self.screen_)
        self.wallGroup_.draw(self.screen_)
        self.gateGroup_.draw(self.screen_)
        if len(self.appleGroup_) > 0:
            self.appleGroup_.draw(self.screen_)
        if len(self.powerUpGroup_) > 0:
            self.powerUpGroup_.draw(self.screen_)
        for ghost in self.ghostGroup_:
            ghost.draw(self.screen_)
        self.scoreCounter_.draw(self.screen_)
        pygame.display.flip()

    def showMainMenuText(self):
        self.render()
        self.mainMenuText_.draw(self.screen_)
        pygame.display.flip()

    def showStartGameText(self):
        self.render()
        self.startgameText_.draw(self.screen_)
        pygame.display.flip()

    def showEndgameText(self):
        if self.gameResult_:
            self.wonGameText_.updateScore(self.scoreCounter_)
            self.wonGameText_.draw(self.screen_)
        else:
            self.lostGameText_.updateScore(self.scoreCounter_)
            self.lostGameText_.draw(self.screen_)
        pygame.display.flip()

    def showPauseText(self):
        self.render()
        self.pauseText_.draw(self.screen_)
        pygame.display.flip()
