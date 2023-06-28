#!/usr/bin/python3

import pygame


def main():
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Pacman")
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


if __name__ == "__main__":
    main()
    pygame.quit()
