'''Snake Game. Contains everything needed to run Snake'''

from snake import Snake

def test_game():
    '''test function'''
    snake = Snake()
    snake.is_alive = True

    for _ in range(1, 5):
        snake.move()
        snake.eat()

if __name__ == '__main__':
    test_game()
