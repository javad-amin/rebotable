from typing import Protocol

from models.position import Position
from models.table import Table


class Robot(Protocol):
    position: Position
    direction: str
    table: Table

    def place(self, position, direction) -> None:
        """Places the robot in the given position and facing the given direction"""

    def move(self) -> None:
        """Moves the robot forward one step towards the facing direction"""

    def rotate_left(self) -> None:
        """Rotates the robot to the left facing the direction defined to be to the left"""

    def rotate_right(self) -> None:
        """Rotates the robot to the right facing the direction defined to be to the left"""

    def report(self) -> str:
        """Reports robots position and the direction that the robot is facing"""
