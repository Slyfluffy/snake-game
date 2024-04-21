'''Game file. Operates the snake game'''
# Imports
import pygame
from time import sleep
from random import randrange

# source imports
from source.color import GameColor
from source.direction import Direction
from source.fruit import Fruit
from source.point import Point
from source.snake import Snake

snake_speed = 15

# size
window_area = (720, 480)

class Game():
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('Curtis Snake')
        self.game_window = pygame.display.set_mode(window_area)
        self.fps = pygame.time.Clock()
        self.score = 0

        # Setup the snake!
        snake_position = Point(100, 50)
        snake_body = [
            Point(100, 50),
            Point(90, 50),
            Point(80, 50),
            Point(70, 50)
        ]
        self.snake = Snake(snake_position, snake_body)

        # Fruit's turn
        self.fruit = Fruit(window_area)

    def display_score(self, color, font:str, size:int) -> None:
        '''Displays the score of the game.
        
        Inputs:
            * color: pygame.Color- the color used for the text (pygame.Color)
            * font: str- The font to be used
            * size: int- the font size to be used
        '''
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score: ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        self.game_window.blit(score_surface, score_rect)

    def game_over(self):
        font = pygame.font.SysFont('times new roman', 50)
        surface = font.render('Your Score is: ' + str(self.score), True, GameColor.RED)
        rect = surface.get_rect()
        rect.midtop = (window_area[0]/2, window_area[1]/4)

        self.game_window.blit(surface, rect)
        pygame.display.flip()

        sleep(2)
        pygame.quit()
        quit()
    
    def get_user_input(self) -> Direction:
        # Set the default direction as wherever the snake is currently going
        direction = self.snake.direction

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    direction = Direction.DOWN
                elif event.key == pygame.K_LEFT:
                    direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    direction = Direction.RIGHT
        
        return direction

    def run_game(self):
        while True:

            # Gather Arrow Key input and change direction accordingly
            direction = self.get_user_input()

            # Move the snake according to the direction
            self.snake.change_direction(direction)
            self.snake.move()

            if self.snake.eat(self.fruit.point):
                self.score += 10
                self.fruit.is_spawned = False

            if not self.fruit.is_spawned:
                self.fruit.set_fruit(window_area)

            self.game_window.fill(GameColor.BLACK)

            # Draw the snake body
            for pos in self.snake.body:
                pygame.draw.rect(self.game_window, GameColor.GREEN, 
                                 pygame.Rect(pos.x, pos.y, 10, 10)
                )

            # Draw the fruit!
            pygame.draw.rect(self.game_window, self.fruit.color, 
                             pygame.Rect(self.fruit.point.x, self.fruit.point.y, 10, 10)
            )

            if self.snake.position.x < 0 or self.snake.position.x > window_area[0]-10:
                self.game_over()
            elif self.snake.position.y < 0 or self.snake.position.y > window_area[1]-10:
                self.game_over()

            for part in self.snake.body[1:]:
                if self.snake.position.x == part.x and self.snake.position.y == part.y:
                    self.game_over()

            self.display_score(GameColor.WHITE, 'times new roman', 20)
            pygame.display.update()
            self.fps.tick(snake_speed)
