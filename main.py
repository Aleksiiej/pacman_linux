#!/usr/bin/python3

import pygame, sys, time
from globalValues import *
from pacman import Pacman
from map import Map


def main():
    pygame.init()
    win = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption("Pacman")
    run = True
    pacman = Pacman()
    map = Map()
    lastTime = time.time()

    while run:
        dt = time.time() - lastTime
        dt *= 60
        pacman.move(dt)
        lastTime = time.time()

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

        win.fill((0, 0, 0))
        pygame.draw.rect(
            win, pacman.Colour, (pacman.x, pacman.y, pacman.width, pacman.height)
        )
        pygame.draw.rect(
            win,
            map.Colour,
            (
                map.obstacle1.x,
                map.obstacle1.y,
                map.obstacle1.width,
                map.obstacle1.height,
            ),
        )
        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
