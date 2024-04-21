
# python imports
from random import randrange

# source imports
from source.color import GameColor
from source.point import Point

FRUIT_COLORS = [
    GameColor.BLUE,
    GameColor.FOREST_GREEN,
    GameColor.ORANGE,
    GameColor.RED,
    GameColor.WHITE,
    GameColor.YELLOW,
]

class Fruit():
    def __init__(self, window_area:tuple) -> None:
        self.set_fruit(window_area)
        
    def set_fruit(self, window_area:tuple) -> None:
        '''Sets the fruit to a new location and marks that it is spawned'''
        rand_x = randrange(1, (window_area[0]//10)) * 10
        rand_y = randrange(1, (window_area[1]//10)) * 10
        self.point = Point(rand_x, rand_y)
        self.is_spawned = True
        self.__set_random_color()

    def __set_random_color(self):
        index = randrange(0, len(FRUIT_COLORS))
        self.color = FRUIT_COLORS[index]