from globalValues import *
from apple import Apple
from wall import Wall


def prepareMap(wallGroup, appleGroup):
    x = 0
    y = 0
    for row in mapInit:
        for el in row:
            if el != 0:
                wallGroup.add(Wall(50, 50, 25 + x * 50, 25 + y * 50, BLUE))
            else:
                appleGroup.add(Apple(20, 20, 25 + x * 50, 25 + y * 50))
            x += 1
        x = 0
        y += 1
