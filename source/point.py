'''Contains the dataclass Point'''

from dataclasses import dataclass

@dataclass
class Point():
    '''Stores the x and y variables marking a point'''
    def __init__(self, x:int=0, y:int=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'The point is ({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'
