from typing import List, Any

from pydantic import BaseModel


class PixelColor(BaseModel):
    r: int
    g: int
    b: int


BLACK = PixelColor(r=0, g=0, b=0)
WHITE = PixelColor(r=255, g=255, b=255)


class Matrix:
    size_x: int
    size_y: int
    pixel: List[PixelColor]

    def __init__(self, size_x, size_y, **data: Any):
        self.size_x = size_x
        self.size_y = size_y
        self.pixel = [BLACK for _ in range(size_x * size_y)]

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
                        f"({pixel.r}, {pixel.g}, {pixel.b})"
                        for pixel in row
                    ]
                )
                for row in self.pixel[::self.size_x]
            ]
        )
