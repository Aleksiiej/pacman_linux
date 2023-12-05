from globalValues import *
from apple import Apple
from wall import Wall


def prepareMap(wallGroup, appleGroup):
    x = 0
    y = 0
    for row in mapInit:
        for el in row:
            if el == 1:
                wallGroup.add(
                    Wall(
                        ENTITY_SIZE,
                        ENTITY_SIZE,
                        ENTITY_SIZE / 2 + x * ENTITY_SIZE,
                        ENTITY_SIZE / 2 + y * ENTITY_SIZE,
                        BLUE,
                    )
                )
            elif el == 2:
                appleGroup.add(
                    Apple(
                        ENTITY_SIZE / 2 + x * ENTITY_SIZE,
                        ENTITY_SIZE / 2 + y * ENTITY_SIZE,
                    )
                )
            else:
                pass
            x += 1
        x = 0
        y += 1
