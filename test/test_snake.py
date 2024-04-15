'''Contains the tests needed to test the functionality of snake.py'''

from source.direction import Direction
from source.point import Point
from source.snake import Snake

class TestSnake:
    '''Contains all the tests for Snake'''

    def test_eat_size_1(self) -> None:
        '''Test the functionality of Snake.eat() from default size of 1'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        assert len(snake.points) == 1

        # EXERCISE
        snake.eat()

        # VERIFY
        assert len(snake.points) == 2

    def test_eat_size_max(self) -> None:
        '''Test how the snake handles getting to max size'''
        # SETUP
        snake = Snake()
        snake.is_alive = True

        for i in range(0, 100):
            point = Point(0, i)
            snake.points.append(point)

        # EXERCISE
        snake.eat()

        # VERIFY
        first_added = snake.points.popleft()
        assert first_added.x == 0
        assert first_added.y == 0

    def test_move_up(self) -> None:
        '''Test the snake moving up'''
        # SETUP
        snake = Snake()
        snake.is_alive = True

        # EXERCISE
        snake.move()

        # VERIFY
        p = snake.points.pop()
        assert p.x == 0
        assert p.y == 1

    def test_move_down(self) -> None:
        '''Test the snake moving moving down'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.move()

        # VERIFY
        p = snake.points.pop()
        assert p.x == 0
        assert p.y == -1

    def test_move_left(self) -> None:
        '''Test the snake moving moving left'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.move()

        # VERIFY
        p = snake.points.pop()
        assert p.x == -1
        assert p.y == 0

    def test_move_right(self) -> None:
        '''Test the snake moving moving right'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.RIGHT

        # EXERCISE
        snake.move()

        # VERIFY
        p = snake.points.pop()
        assert p.x == 1
        assert p.y == 0

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
        snake = Snake()
        snake.is_alive = True

        # EXERCISE
        snake.change_direction(Direction.UP)

        # VERIFY
        assert snake.direction == Direction.UP

    def test_change_direction_up_no_change_down(self) -> None:
        '''Test that snake makes no changes when set to up and trying to change to down'''
        # SETUP
        snake = Snake()
        snake.is_alive = True

        # EXERCISE
        snake.change_direction(Direction.DOWN)

        # VERIFY
        assert snake.direction == Direction.UP

    def test_change_direction_up_change_left(self) -> None:
        '''Test that snake makes no changes when from up to left'''
        # SETUP
        snake = Snake()
        snake.is_alive = True

        # EXERCISE
        snake.change_direction(Direction.LEFT)

        # VERIFY
        assert snake.direction == Direction.LEFT

    def test_change_direction_up_change_right(self) -> None:
        '''Test that snake makes no changes when from up to right'''
        # SETUP
        snake = Snake()
        snake.is_alive = True

        # EXERCISE
        snake.change_direction(Direction.RIGHT)

        # VERIFY
        assert snake.direction == Direction.RIGHT

    def test_change_direction_down_no_change(self) -> None:
        '''Test that snake makes no changes when set to down and trying to change to down'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.change_direction(Direction.DOWN)

        # VERIFY
        assert snake.direction == Direction.DOWN

    def test_change_direction_down_no_change_up(self) -> None:
        '''Test that snake makes no changes when set to down and trying to change to up'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.change_direction(Direction.UP)

        # VERIFY
        assert snake.direction == Direction.DOWN

    def test_change_direction_down_change_left(self) -> None:
        '''Test that snake makes no changes when from down to left'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.change_direction(Direction.LEFT)

        # VERIFY
        assert snake.direction == Direction.LEFT

    def test_change_direction_down_change_right(self) -> None:
        '''Test that snake makes no changes when from down to right'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.DOWN

        # EXERCISE
        snake.change_direction(Direction.RIGHT)

        # VERIFY
        assert snake.direction == Direction.RIGHT

    def test_change_direction_left_no_change(self) -> None:
        '''Test that snake makes no changes when set to left and trying to change to left'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.change_direction(Direction.LEFT)

        # VERIFY
        assert snake.direction == Direction.LEFT

    def test_change_direction_left_no_change_right(self) -> None:
        '''Test that snake makes no changes when set to left and trying to change to right'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.change_direction(Direction.RIGHT)

        # VERIFY
        assert snake.direction == Direction.LEFT

    def test_change_direction_left_change_up(self) -> None:
        '''Test that snake makes no changes when from left to up'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.change_direction(Direction.UP)

        # VERIFY
        assert snake.direction == Direction.UP

    def test_change_direction_left_change_down(self) -> None:
        '''Test that snake makes no changes when from left to down'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.LEFT

        # EXERCISE
        snake.change_direction(Direction.DOWN)

        # VERIFY
        assert snake.direction == Direction.DOWN

    def test_change_direction_right_no_change(self) -> None:
        '''Test that snake makes no changes when set to right and trying to change to right'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.RIGHT

        # EXERCISE
        snake.change_direction(Direction.RIGHT)

        # VERIFY
        assert snake.direction == Direction.RIGHT

    def test_change_direction_right_no_change_left(self) -> None:
        '''Test that snake makes no changes when set to right and trying to change to left'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.RIGHT

        # EXERCISE
        snake.change_direction(Direction.LEFT)

        # VERIFY
        assert snake.direction == Direction.RIGHT

    def test_change_direction_right_change_up(self) -> None:
        '''Test that snake makes no changes when from right to up'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.RIGHT

        # EXERCISE
        snake.change_direction(Direction.UP)

        # VERIFY
        assert snake.direction == Direction.UP

    def test_change_direction_right_change_down(self) -> None:
        '''Test that snake makes no changes when from right to down'''
        # SETUP
        snake = Snake()
        snake.is_alive = True
        snake.direction = Direction.RIGHT

        # EXERCISE
        snake.change_direction(Direction.DOWN)

        # VERIFY
        assert snake.direction == Direction.DOWN
