from dataclasses import dataclass


@dataclass
class HIQPosition:
    x: int = 0
    y: int = 0

    def __add__(self, pos):
        return HIQPosition(
            self.x + pos.x,
            self.y + pos.y,
        )

    def __str__(self):
        return f"{self.x},{self.y}"
