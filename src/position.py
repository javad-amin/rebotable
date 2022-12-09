from dataclasses import dataclass


@dataclass
class Position:
    x: int = 0
    y: int = 0

    def __add__(self, pos):
        return Position(
            self.x + pos.x,
            self.y + pos.y,
        )

    def __str__(self):
        return f"{self.x},{self.y}"
