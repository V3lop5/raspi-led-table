from game import Game
from matrix import Matrix


class Snake(Game):
    def __init__(self, matrix: Matrix):
        super().__init__(matrix=matrix)
