#!/usr/bin/python3

import pygame
from pacman import Pacman


def main():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Pacman")
    run = True
    pacman = Pacman()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.draw.rect(
            win, pacman.Colour, (pacman.x, pacman.y, pacman.width, pacman.height)
        )
        pygame.display.update()


if __name__ == "__main__":
    main()
    pygame.quit()
