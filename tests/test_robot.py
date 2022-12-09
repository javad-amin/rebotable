import pytest

from exceptions import PositionOutsideTable, RobotNotPlacedYet, UnknownDirection
from position import Position
from robot import Robot


def test_robot_not_placed_on_table() -> None:
    """Test that a robot can be initialized outside the table"""
    robot = Robot()

    assert robot.position == Position(-1, -1)
    assert robot.direction == "NORTH"


def test_robot_place_outside_table() -> None:
    """Test attempting to place a robot in a position outside the table"""
    robot = Robot()
    position_outside_table = Position(5, 5)

    with pytest.raises(
        PositionOutsideTable,
        match="The robot cannot be placed outside of the table.",
    ):
        robot.place(position_outside_table, "NORTH")


def test_robot_place_on_table_unknown_direction() -> None:
    """Test attempting to place a robot in a position on the table"""
    robot = Robot()
    position_on_table = Position(3, 2)
    new_direction = "SOUTHWEST"

    with pytest.raises(UnknownDirection, match="The given location is unknown"):
        robot.place(position_on_table, new_direction)


def test_robot_place_on_table() -> None:
    """Test attempting to place a robot in a position on the table"""
    robot = Robot()
    position_on_table = Position(3, 2)
    new_direction = "WEST"

    robot.place(position_on_table, new_direction)
    assert robot.position == position_on_table
    assert robot.direction == new_direction


def test_robot_move_towards_direction_not_placed_yet() -> None:
    """Test moving the robot forward when it's not placed yet"""
    robot = Robot()

    with pytest.raises(
        RobotNotPlacedYet,
        match="MOVE Command not accepted! Place the robot first by: PLACE <x_position>,<y_position>,<direction>",
    ):
        robot.move()


def test_robot_move_towards_direction_would_fall_from_table() -> None:
    """Test moving forward should be blocked when placement is outside of table"""
    robot = Robot()
    robot.place(Position(0, 0), "SOUTH")

    with pytest.raises(
        PositionOutsideTable,
        match="The robot cannot be placed outside of the table.",
    ):
        robot.move()


def test_robot_move_towards_direction_successfully() -> None:
    """Test moving the robot forward when placed and moving is allowed"""
    robot = Robot()

    robot.place(Position(1, 1), "NORTH")
    robot.move()
    assert robot.position == Position(1, 2)

    robot.place(Position(1, 1), "WEST")
    robot.move()
    assert robot.position == Position(0, 1)

    robot.place(Position(1, 1), "EAST")
    robot.move()
    assert robot.position == Position(2, 1)

    robot.place(Position(1, 1), "SOUTH")
    robot.move()
    assert robot.position == Position(1, 0)


def test_robot_rotate__left_unplaced_robot() -> None:
    """Test rotate left unplaced robot"""
    robot = Robot()

    with pytest.raises(
        RobotNotPlacedYet,
        match="LEFT Command not accepted! Place the robot first by: PLACE <x_position>,<y_position>,<direction>",
    ):
        robot.rotate_left()


def test_robot_rotate_left() -> None:
    """Test rotate the robot to the left all possible scenarios"""
    robot = Robot()
    robot.place(Position(1, 1), "NORTH")

    robot.rotate_left()
    assert robot.direction == "WEST"

    robot.rotate_left()
    assert robot.direction == "SOUTH"

    robot.rotate_left()
    assert robot.direction == "EAST"

    robot.rotate_left()
    assert robot.direction == "NORTH"


def test_robot_rotate_right_unplaced_robot() -> None:
    """Test rotate left unplaced robot"""
    robot = Robot()

    with pytest.raises(
        RobotNotPlacedYet,
        match="RIGHT Command not accepted! Place the robot first by: PLACE <x_position>,<y_position>,<direction>",
    ):
        robot.rotate_right()


def test_robot_rotate_right() -> None:
    """Test rotate the robot to the right all possible scenarios"""
    robot = Robot()
    robot.place(Position(1, 1), "NORTH")

    robot.rotate_right()
    assert robot.direction == "EAST"

    robot.rotate_right()
    assert robot.direction == "SOUTH"

    robot.rotate_right()
    assert robot.direction == "WEST"

    robot.rotate_right()
    assert robot.direction == "NORTH"

    def __str__(self) -> str:
        return f"{self.position},{self.facing}"


def test_string_representation_of_a_position() -> None:
    """Tests that the string representation of a position is as desireable"""
    robot = Robot()
    robot.place(Position(3, 4), "WEST")

    assert str(robot) == "3,4,WEST"
