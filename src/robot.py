from dataclasses import dataclass

from exceptions import PositionOutsideTable, RobotNotPlacedYet, UnknownDirection
from position import Position
from table import Table

DIRECTION_MOVEMENT_MAP = {
    "NORTH": Position(0, 1),
    "EAST": Position(1, 0),
    "SOUTH": Position(0, -1),
    "WEST": Position(-1, 0),
}


@dataclass
class Robot:
    position: Position = Position(-1, -1)
    direction: str = "NORTH"
    table: Table = Table(5, 5)

    def place(self, position, direction) -> None:
        """Places the robot in the given position and facing the given direction

        Example:
            position = Position(1, 2)
            direction = "SOUTH"
            Places the robot in position x=1, y=2 facing southwards.
        """
        if not self.table.is_on_table(position):
            raise PositionOutsideTable(
                "The robot cannot be placed outside of the table."
            )
        if direction not in DIRECTION_MOVEMENT_MAP:
            raise UnknownDirection("The given location is unknown")
        self.position = position
        self.direction = direction

    def move(self) -> None:
        """Moves the robot forward one step towards the facing direction"""
        if self.position == Position(-1, -1):
            raise RobotNotPlacedYet(
                "MOVE Command not accepted! Place the robot first by: PLACE <x_position>,<y_position>,<direction>"
            )
        new_position = self.position + DIRECTION_MOVEMENT_MAP[self.direction]
        self.place(new_position, self.direction)
