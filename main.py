import pygame
from globalValues import *
from pacman import Pacman
from map import prepareMap
from drawFacade import DrawFacade
from scoreCounter import ScoreCounter

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()

pacman = Pacman(50, 50, 75, 75, False)
wallGroup = pygame.sprite.Group()
appleGroup = pygame.sprite.Group()
prepareMap(wallGroup, appleGroup)
drawFacade = DrawFacade(screen, pacman, wallGroup, appleGroup, pygame)

run = True
while run:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    pacman.proposedDir = Direction.UP
                case pygame.K_DOWN:
                    pacman.proposedDir = Direction.DOWN
                case pygame.K_LEFT:
                    pacman.proposedDir = Direction.LEFT
                case pygame.K_RIGHT:
                    pacman.proposedDir = Direction.RIGHT
                case pygame.K_ESCAPE:
                    run = False

    pacman.update(wallGroup)
    for apple in appleGroup:
        if apple.rect.colliderect(pacman):  # only one collision per FPS possible
            appleGroup.remove(apple)
            if len(appleGroup) == 0:
                run = False
            ScoreCounter.incrementScore()
            break

    drawFacade.drawGame()

pygame.quit()
