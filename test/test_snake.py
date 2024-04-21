'''Contains the tests needed to test the functionality of snake.py'''

from source.direction import Direction
from source.point import Point
from source.snake import Snake

class TestSnake:
    '''Contains all the tests for Snake'''

    def test_eat_size_4(self) -> None:
        '''Test the functionality of Snake.eat() from default size of 4'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        assert len(snake.body) == 4

        # EXERCISE
        fruit_point = Point(0, 0)
        snake.eat(fruit_point)

        # VERIFY
        assert len(snake.body) == 5

    def test_move_up(self) -> None:
        '''Test the snake moving up'''
        # SETUP
        position = Point(100, 50)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.UP

        # EXERCISE
        snake.move()

        # VERIFY
        assert snake.position.x == 100
        assert snake.position.y == 40

    def test_move_down(self) -> None:
        '''Test the snake moving moving down'''
        # SETUP
        position = Point(100, 50)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.move()

        # VERIFY
        assert snake.position.x == 100
        assert snake.position.y == 60

    def test_move_left(self) -> None:
        '''Test the snake moving moving left'''
        # SETUP
        position = Point(100, 50)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.move()

        # VERIFY
        assert snake.position.x == 90
        assert snake.position.y == 50

    def test_move_right(self) -> None:
        '''Test the snake moving moving right'''
        # SETUP
        position = Point(100, 50)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)

        # EXERCISE
        snake.move()

        # VERIFY
        assert snake.position.x == 110
        assert snake.position.y == 50

    def test_test(self) -> None:
        '''template'''
        # SETUP
        # EXERCISE
        # VERIFY

class TestSnakeDirection:
    '''Contains all the tests for Snake's change_direction class'''
    def test_change_direction_up_no_change(self) -> None:
        '''Test that snake makes no changes when set to up and trying to change to up'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.UP

        # EXERCISE
        snake.change_direction(Direction.UP)

        # VERIFY
        assert snake.direction == Direction.UP

    def test_change_direction_up_no_change_down(self) -> None:
        '''Test that snake makes no changes when set to up and trying to change to down'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.UP

        # EXERCISE
        snake.change_direction(Direction.DOWN)

        # VERIFY
        assert snake.direction == Direction.UP

    def test_change_direction_up_change_left(self) -> None:
        '''Test that snake makes no changes when from up to left'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.UP

        # EXERCISE
        snake.change_direction(Direction.LEFT)

        # VERIFY
        assert snake.direction == Direction.LEFT

    def test_change_direction_up_change_right(self) -> None:
        '''Test that snake makes no changes when from up to right'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.UP

        # EXERCISE
        snake.change_direction(Direction.RIGHT)

        # VERIFY
        assert snake.direction == Direction.RIGHT

    def test_change_direction_down_no_change(self) -> None:
        '''Test that snake makes no changes when set to down and trying to change to down'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.change_direction(Direction.DOWN)

        # VERIFY
        assert snake.direction == Direction.DOWN

    def test_change_direction_down_no_change_up(self) -> None:
        '''Test that snake makes no changes when set to down and trying to change to up'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.change_direction(Direction.UP)

        # VERIFY
        assert snake.direction == Direction.DOWN

    def test_change_direction_down_change_left(self) -> None:
        '''Test that snake makes no changes when from down to left'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.change_direction(Direction.LEFT)

        # VERIFY
        assert snake.direction == Direction.LEFT

    def test_change_direction_down_change_right(self) -> None:
        '''Test that snake makes no changes when from down to right'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.change_direction(Direction.RIGHT)

        # VERIFY
        assert snake.direction == Direction.RIGHT

    def test_change_direction_left_no_change(self) -> None:
        '''Test that snake makes no changes when set to left and trying to change to left'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.change_direction(Direction.LEFT)

        # VERIFY
        assert snake.direction == Direction.LEFT

    def test_change_direction_left_no_change_right(self) -> None:
        '''Test that snake makes no changes when set to left and trying to change to right'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.change_direction(Direction.RIGHT)

        # VERIFY
        assert snake.direction == Direction.LEFT

    def test_change_direction_left_change_up(self) -> None:
        '''Test that snake makes no changes when from left to up'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.change_direction(Direction.UP)

        # VERIFY
        assert snake.direction == Direction.UP

    def test_change_direction_left_change_down(self) -> None:
        '''Test that snake makes no changes when from left to down'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.change_direction(Direction.DOWN)

        # VERIFY
        assert snake.direction == Direction.DOWN

    def test_change_direction_right_no_change(self) -> None:
        '''Test that snake makes no changes when set to right and trying to change to right'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)

        # EXERCISE
        snake.change_direction(Direction.RIGHT)

        # VERIFY
        assert snake.direction == Direction.RIGHT

    def test_change_direction_right_no_change_left(self) -> None:
        '''Test that snake makes no changes when set to right and trying to change to left'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)

        # EXERCISE
        snake.change_direction(Direction.LEFT)

        # VERIFY
        assert snake.direction == Direction.RIGHT

    def test_change_direction_right_change_up(self) -> None:
        '''Test that snake makes no changes when from right to up'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)

        # EXERCISE
        snake.change_direction(Direction.UP)

        # VERIFY
        assert snake.direction == Direction.UP

    def test_change_direction_right_change_down(self) -> None:
        '''Test that snake makes no changes when from right to down'''
        # SETUP
        position = Point(0, 0)
        body = [Point(0,0), Point(0,0), Point(0,0), Point(0,0)]
        snake = Snake(position, body)

        # EXERCISE
        snake.change_direction(Direction.DOWN)

        # VERIFY
        assert snake.direction == Direction.DOWN
