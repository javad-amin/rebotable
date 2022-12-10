from typing import Protocol

from models.position import Position


class Table(Protocol):
    width: int
    height: int

    def is_on_table(self, position: Position) -> bool:
        """Check if object is on table"""
