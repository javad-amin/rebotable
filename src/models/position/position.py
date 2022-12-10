from typing import Protocol


class Position(Protocol):
    x: int
    y: int

    def __add__(self, pos):
        """Add two positions together"""
