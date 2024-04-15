'''Contains the Direction class which is used to list the various movable directions'''
from enum import Enum

class Direction(Enum):
    '''Enum class listing the possible directions of movement.'''
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
