import enum
from typing import List, Any


class PixelColor(enum.Enum):
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)


class Matrix:
    size_x: int
    size_y: int
    pixel: List[PixelColor]

    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y
        self.pixel = [PixelColor.BLACK for _ in range(size_x * size_y)]

    def set_pixel(self, x, y, color):
        if (x < 0 or x >= self.size_x) or (y < 0 or y >= self.size_y):
            raise IndexError("Index out of range")
        self.pixel[x + y * self.size_x] = color

    def get_pixel(self, x, y) -> PixelColor:
        if (x < 0 or x >= self.size_x) or (y < 0 or y >= self.size_y):
            raise IndexError("Index out of range")
        return self.pixel[x + y * self.size_x]

    def set_all(self, color):
        self.pixel = [color for _ in range(self.size_x * self.size_y)]

    def __str__(self):
        return "\n".join(
            [
                " ".join(
                    [
                        str(self.get_pixel(x, y))
                        for x in range(self.size_x)
                    ]
                )
                for y in range(self.size_y)
            ]
        )
