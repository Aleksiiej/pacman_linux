import pygame
from globalValues import *
from pacman import Pacman
from apple import Apple
from map import prepareMap

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()

pacman = Pacman(50, 50, 75, 75, False)

wallGroup = pygame.sprite.Group()
appleGroup = pygame.sprite.Group()
prepareMap(wallGroup, appleGroup)

appleList = []
appleList.append(Apple(20, 20, 75, 125))

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

    pacman.update(wallGroup, screen)
    wallGroup.draw(screen)
    for apple in appleGroup:
        if apple.rect.colliderect(pacman):
            appleGroup.remove(apple)
        else:
            apple.update(screen)
    pygame.display.flip()

pygame.quit()
