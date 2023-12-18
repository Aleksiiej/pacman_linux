from globalValues import *
from map.wall import Wall
from map.apple import Apple
from map.powerUp import PowerUp


def prepareMap(wallGroup, appleGroup, powerUpGroup):
    x = 0
    y = 0
    for row in mapInit:
        for el in row:
            match el:
                case 1:
                    wallGroup.add(
                        Wall(
                            ENTITY_SIZE,
                            ENTITY_SIZE,
                            ENTITY_SIZE / 2 + x * ENTITY_SIZE,
                            ENTITY_SIZE / 2 + y * ENTITY_SIZE,
                            BLUE,
                        )
                    )
                case 2:
                    appleGroup.add(
                        Apple(
                            ENTITY_SIZE / 2 + x * ENTITY_SIZE,
                            ENTITY_SIZE / 2 + y * ENTITY_SIZE,
                        )
                    )
                case 3:
                    powerUpGroup.add(
                        PowerUp(
                            ENTITY_SIZE / 2 + x * ENTITY_SIZE,
                            ENTITY_SIZE / 2 + y * ENTITY_SIZE,
                        )
                    )
            x += 1
        x = 0
        y += 1
