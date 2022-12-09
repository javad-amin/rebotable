from position import Position
from robot import Robot

TABLE_SIZE = 5


def test_robot_not_placed_on_table() -> None:
    robot = Robot()

    assert robot.position == Position(-1, -1)
    assert robot.direction == "North"
