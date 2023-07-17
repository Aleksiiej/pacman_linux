import pygame
from globalValues import *
from wall import Wall


class Map(pygame.sprite.Sprite):
    def __init__(self, wallGroup):
        self.walls = []
        for i in range(16):
            wall = self.walls.append(Wall(50, 50, 75 + 50 * i, 75, BLUE))
        for i in range(16):
            wall = self.walls.append(Wall(50, 50, 75 + 50 * i, 825, BLUE))
        for i in range(14):
            wall = self.walls.append(Wall(50, 50, 75, 125 + 50 * i, BLUE))
        for i in range(14):
            wall = self.walls.append(Wall(50, 50, 825, 125 + 50 * i, BLUE))
        for wall in self.walls:
            wallGroup.add(wall)