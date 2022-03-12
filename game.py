from typing import Any

from key import Key
from matrix import Matrix


class Game:
    """
    Basic class for all games.
    """
    name: str = 'Unnamed Game'
    description: str = 'No description'
    game_over = False
    size_x: int
    size_y: int

    def __init__(self, matrix: Matrix):
        self.size_x = matrix.size_x
        self.size_y = matrix.size_y

    def on_key_press(self, key: Key):
        """
        Method to handle key presses.
        """
        pass

    def update_matrix(self, matrix: Matrix):
        """
        Method to update the matrix every tick.
        """
        pass
