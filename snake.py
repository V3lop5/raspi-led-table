import enum
import random
from typing import List, Optional

from game import Game
from key import Key
from matrix import Matrix, PixelColor

BACKGROUND_COLOR = PixelColor.BLACK
FOOD_COLOR = PixelColor.GREEN
SNAKE_COLOR = PixelColor.RED


class SnakeDirection(enum.Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Snake(Game):
    """
    A simple snake game implementation.
    Eat the food to grow and don't hit the walls or yourself.

    The snake is controlled by the arrow keys.
    """
    snake_head = [0, 0]
    snake_body = []

    food_spawn = False
    food_pos = [0, 0]

    direction = SnakeDirection.DOWN
    change_to = direction

    score = 0

    def __init__(self, matrix: Matrix):
        super().__init__(matrix)
        self.create_initial_snake_body()
        matrix.set_all(BACKGROUND_COLOR)
        for x, y in self.snake_body:
            matrix.set_pixel(x, y, SNAKE_COLOR)

    def create_initial_snake_body(self):
        """
        Creates the initial body of the snake.
        The initial body is 4 pixels long
        """
        self.snake_head = [self.size_x // 2, max(self.size_y // 2 - 3, 0)]
        for i in range(3):
            self.snake_body.insert(0, list(self.snake_head))
            self.update_snake_head_position()
        self.snake_body.insert(0, list(self.snake_head))

    def spawn_new_food(self):
        """
        Spawns a new food at a random position.
        If food is spawned on top of the snake, the food is respawned at a random position.

        :return:
        """
        while not self.food_spawn:
            self.food_pos = [random.randrange(0, self.size_x - 1), random.randrange(0, self.size_y - 1)]
            print('Try food spawn at: ', self.food_pos)
            if self.food_pos not in self.snake_body:
                self.food_spawn = True

    def update_snake_direction(self):
        """
        Updates the direction of the snake if possible.
        Prevents the snake from turning 180 degrees.
        """
        if self.change_to == SnakeDirection.UP and self.direction != SnakeDirection.DOWN:
            self.direction = SnakeDirection.UP
        elif self.change_to == SnakeDirection.DOWN and self.direction != SnakeDirection.UP:
            self.direction = SnakeDirection.DOWN
        elif self.change_to == SnakeDirection.LEFT and self.direction != SnakeDirection.RIGHT:
            self.direction = SnakeDirection.LEFT
        elif self.change_to == SnakeDirection.RIGHT and self.direction != SnakeDirection.LEFT:
            self.direction = SnakeDirection.RIGHT

    def update_snake_head_position(self):
        """
        Updates the position of the snake head according to the current direction.
        """
        if self.direction == SnakeDirection.UP:
            self.snake_head[1] -= 1
        elif self.direction == SnakeDirection.DOWN:
            self.snake_head[1] += 1
        elif self.direction == SnakeDirection.LEFT:
            self.snake_head[0] -= 1
        elif self.direction == SnakeDirection.RIGHT:
            self.snake_head[0] += 1

    def update_snake_body(self) -> Optional[List[int]]:
        """
        Updates the snake body.

        :return: The tail pixel that is removed from the snake body.
        """
        self.snake_body.insert(0, list(self.snake_head))
        if self.snake_head[0] == self.food_pos[0] and self.snake_head[1] == self.food_pos[1]:
            self.food_spawn = False
            self.score += 1
            return None
        return self.snake_body.pop()

    def check_game_over(self) -> bool:
        """
        Checks if the game is over.
        The game is over if the snake hits the wall or itself.

        :return:
        """
        if self.snake_head[0] < 0 or self.snake_head[0] >= self.size_x \
                or self.snake_head[1] < 0 or self.snake_head[1] >= self.size_y:
            return True
        if self.snake_head in self.snake_body[1:]:
            return True
        return False

    def update_matrix(self, matrix: Matrix):
        """
        Called every tick of the game loop to update snake game state.

        Updates snake direction, moves snake head, collects food, moves tail and checks for game over.
        """
        self.update_snake_direction()
        self.update_snake_head_position()
        old_tail = self.update_snake_body()

        if not self.food_spawn:
            self.spawn_new_food()

        if self.check_game_over():
            self.game_over = True
            print('Game over!')
            return

        # Update matrix
        matrix.set_pixel(self.food_pos[0], self.food_pos[1], FOOD_COLOR)
        matrix.set_pixel(self.snake_head[0], self.snake_head[1], SNAKE_COLOR)
        if old_tail is not None:
            matrix.set_pixel(old_tail[0], old_tail[1], BACKGROUND_COLOR)

    def on_key_press(self, key: Key):
        """
        Updates the next direction of the snake if the key press is valid.
        Prevents the snake from reversing direction.

        :param key: Key that was pressed.
        """
        if key == Key.ARROW_UP and self.direction != SnakeDirection.DOWN:
            self.change_to = SnakeDirection.UP
        elif key == Key.ARROW_DOWN and self.direction != SnakeDirection.UP:
            self.change_to = SnakeDirection.DOWN
        elif key == Key.ARROW_LEFT and self.direction != SnakeDirection.RIGHT:
            self.change_to = SnakeDirection.LEFT
        elif key == Key.ARROW_RIGHT and self.direction != SnakeDirection.LEFT:
            self.change_to = SnakeDirection.RIGHT
