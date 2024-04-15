'''Contains the Snake class, which handles everything to operate the snake'''

# Python imports
from collections import deque

# custom imports
from source.point import Point
from source.direction import Direction

class Snake():
    '''Contains the logic and data in order for the snake to operate'''
    def __init__(self) -> None:
        self.is_alive:bool = False
        self.direction:Direction = Direction.UP
        self.__size_max = 100
        self.__head_point = Point(0, 0)
        self.points:deque[Point] = deque(maxlen=self.__size_max)
        self.points.append(self.__head_point)

    def eat(self) -> None:
        '''Snake eats, growing in size by one'''
        if self.is_alive and len(self.points) != self.__size_max:
            self.points.append(self.__head_point)
            print(f"Adding point: {repr(self.__head_point)}")

    def change_direction(self, direction:Direction):
        '''Changes the direction of movement from the snake'''
        if direction == Direction.UP and self.direction == Direction.DOWN:
            return
        if direction == Direction.DOWN and self.direction == Direction.UP:
            return
        if direction == Direction.LEFT and self.direction == Direction.RIGHT:
            return
        if direction == Direction.RIGHT and self.direction == Direction.LEFT:
            return

        self.direction = direction

    def move(self) -> None:
        '''Move the snake depending on the direction selected'''
        if not self.is_alive:
            return

        direction = self.direction
        match direction:
            case Direction.UP:
                point = Point(self.__head_point.x, self.__head_point.y + 1)
            case Direction.DOWN:
                point = Point(self.__head_point.x, self.__head_point.y - 1)
            case Direction.LEFT:
                point = Point(self.__head_point.x - 1, self.__head_point.y)
            case Direction.RIGHT:
                point = Point(self.__head_point.x + 1, self.__head_point.y)

        print(f"Moving to point {repr(point)}")
        self.__head_point = point
        self.points.append(point)
        self.points.popleft()
        print(self.points)
