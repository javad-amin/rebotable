from collections import OrderedDict
from dataclasses import dataclass

from exceptions import PositionOutsideTable, RobotNotPlacedYet, UnknownDirection
from position import Position
from table import Table

DIRECTION_MOVEMENT_MAP = OrderedDict(
    (
        ("NORTH", Position(0, 1)),
        ("EAST", Position(1, 0)),
        ("SOUTH", Position(0, -1)),
        ("WEST", Position(-1, 0)),
    )
)


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
        self._check_if_robot_is_placed("MOVE")
        new_position = self.position + DIRECTION_MOVEMENT_MAP[self.direction]
        self.place(new_position, self.direction)

    def rotate_left(self) -> None:
        """Rotates the robot to the left facing the direction defined to be to the left"""
        self._check_if_robot_is_placed("LEFT")
        directions = list(DIRECTION_MOVEMENT_MAP.keys())
        current_direction_index = directions.index(self.direction)
        self.direction = directions[current_direction_index - 1]

    def rotate_right(self) -> None:
        """Rotates the robot to the right facing the direction defined to be to the left"""
        self._check_if_robot_is_placed("RIGHT")
        directions = list(DIRECTION_MOVEMENT_MAP.keys())
        current_direction_index = directions.index(self.direction)
        new_direction_index = current_direction_index + 1
        if new_direction_index > len(directions) - 1:
            self.direction = directions[0]
        else:
            self.direction = directions[new_direction_index]

    def report(self) -> str:
        """Reports robots position and the direction that the robot is facing"""
        self._check_if_robot_is_placed("REPORT")
        return f"{str(self.position)},{self.direction}"

    def _check_if_robot_is_placed(self, command: str) -> None:
        if not self.table.is_on_table(self.position):
            raise RobotNotPlacedYet(
                f"{command.upper()} Command not accepted! Place the robot first by: PLACE <x_position>,<y_position>,<direction>"
            )
