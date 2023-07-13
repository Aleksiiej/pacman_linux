#!/usr/bin/python3

import pygame
from globalValues import *
from pacman import Pacman
from wall import Wall


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Pacman")

pacmanGroup = pygame.sprite.Group()
pacman = Pacman(50, 50, 450, 450, RED)
pacmanGroup.add(pacman)

wallGroup = pygame.sprite.Group()
wall1 = Wall(50, 50, 75, 75, BLUE)
wallGroup.add(wall1)

run = True
while run:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_UP:
                    pacman.changeDirToUp()
                case pygame.K_DOWN:
                    pacman.changeDirToDown()
                case pygame.K_LEFT:
                    pacman.changeDirToLeft()
                case pygame.K_RIGHT:
                    pacman.changeDirToRight()
                case pygame.K_ESCAPE:
                    run = False

    pacmanGroup.update(wallGroup)
    wallGroup.draw(screen)
    pacmanGroup.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)
pygame.quit()