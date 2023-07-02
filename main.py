#!/usr/bin/python3

import pygame
from globalValues import *
from pacman import Pacman


def main():
    pygame.init()
    win = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption("Pacman")
    run = True
    pacman = Pacman()

    while run:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            pacman.moveLeft()
        if keys[pygame.K_RIGHT]:
            pacman.moveRight()
        if keys[pygame.K_UP]:
            pacman.moveUp()
        if keys[pygame.K_DOWN]:
            pacman.moveDown()

        win.fill((0, 0, 0))
        pygame.draw.rect(
            win, pacman.Colour, (pacman.x, pacman.y, pacman.width, pacman.height)
        )
        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
