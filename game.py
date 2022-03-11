from typing import Any

from key import Key
from matrix import Matrix


class Game:
    """
    Basic class for all games.
    """
    name: str = 'Unnamed Game'
    description: str = 'No description'
    matrix: Matrix = None

    def __init__(self, matrix: Matrix, **data: Any):
        super().__init__(**data)
        self.matrix = matrix

    def on_key_press(self, key: Key):
        """
        Method to handle key presses.
        """
        pass

    def on_tick(self):
        """
        Method to handle ticks.
        """
        pass
