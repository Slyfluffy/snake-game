'''Contains the Snake class, which handles everything to operate the snake'''

# custom imports
from source.direction import Direction
from source.point import Point

class Snake():
    '''Contains the logic and data in order for the snake to operate'''
    def __init__(self, position: Point, body:list[Point]) -> None:
        self.direction:Direction = Direction.RIGHT
        self.position = position
        self.body = body

    def eat(self, fruit_point: Point) -> bool:
        '''Snake eats, growing in size by one'''
        self.body.insert(0, Point(self.position.x, self.position.y))
        if self.position == fruit_point and self.position == fruit_point:
            return True
        else:
            self.body.pop()
            return False

    def change_direction(self, new_direction:Direction):
        '''Changes the direction of movement from the snake'''
        if new_direction == Direction.UP and self.direction == Direction.DOWN:
            return
        if new_direction == Direction.DOWN and self.direction == Direction.UP:
            return
        if new_direction == Direction.LEFT and self.direction == Direction.RIGHT:
            return
        if new_direction == Direction.RIGHT and self.direction == Direction.LEFT:
            return

        self.direction = new_direction

    def move(self) -> None:
        '''Move the snake depending on the direction selected'''
        if self.direction == Direction.UP:
            self.position.y -= 10
        elif self.direction == Direction.DOWN:
            self.position.y += 10
        elif self.direction == Direction.LEFT:
            self.position.x -= 10
        elif self.direction == Direction.RIGHT:
            self.position.x += 10
