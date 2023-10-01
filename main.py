import pygame
from globalValues import *
from pacman import Pacman
from map import prepareMap

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption("Pacman")
clock = pygame.time.Clock()

pacmanImages = []
for i in range(1, 5):
    pacmanImages.append(
        pygame.transform.scale(
            pygame.image.load(f"assets/pacman_images/{i}.png"), (50, 50)
        )
    )
pacman = Pacman(50, 50, 75, 75, pacmanImages)

wallGroup = pygame.sprite.Group()
prepareMap(wallGroup)

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
    pygame.display.flip()

pygame.quit()
