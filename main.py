#!/usr/bin/python3

import pygame, sys, time
from globalValues import *
from pacman import Pacman


def main():
    pygame.init()
    win = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption("Pacman")
    run = True
    pacman = Pacman(RED, 40, 40)
    allSpritesList = pygame.sprite.Group()
    allSpritesList.add(pacman)
    clock = pygame.time.Clock()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pacman.changeDirToLeft()
        if keys[pygame.K_RIGHT]:
            pacman.changeDirToRight()
        if keys[pygame.K_UP]:
            pacman.changeDirToUp()
        if keys[pygame.K_DOWN]:
            pacman.changeDirToDown()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        
        pacman.move()

        win.fill((0, 0, 0))
        allSpritesList.draw(win)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
    pygame.quit()
