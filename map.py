import pygame
from globalValues import *
from wall import Wall


class Map(pygame.sprite.Sprite):
    def __init__(self, wallGroup):
        self.walls = []
        x = 0
        y = 0
        for row in mapInit:
            for el in row:
                if el != 0:
                    self.walls.append(Wall(50, 50, 25 + x * 50, 25 + y * 50, BLUE))
                x += 1
            x = 0
            y += 1

        for wall in self.walls:
            wallGroup.add(wall)
