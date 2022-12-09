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
    """Test moving the robot forward when it's not placed yet"""
    robot = Robot()
    robot.place(Position(0, 0), "SOUTH")

    with pytest.raises(
        PositionOutsideTable,
        match="The robot cannot be placed outside of the table.",
    ):
        robot.move()


def test_robot_move_towards_direction_successfully() -> None:
    """Test moving the robot forward when it's not placed yet"""
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


def test_robot_rotate_left() -> None:
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


def test_robot_rotate_right() -> None:
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
