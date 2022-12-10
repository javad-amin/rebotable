import logging
from typing import Optional

from models.commands.parse import ParsedCommand
from models.position import HIQPosition
from models.robot import Robot
from models.robot.exceptions import (
    PositionOutsideTable,
    RobotNotPlacedYet,
    UnknownDirection,
)


def route_command(
    line_number: int,
    parsed_command: ParsedCommand,
    robot: Robot,
) -> str:
    """Commands router takes care of running the commands and handles exceptions provides report"""
    report = ""
    if parsed_command.command.upper() == "PLACE":
        try:
            robot.place(
                position=HIQPosition(parsed_command.x, parsed_command.y),
                direction=parsed_command.direction,
            )
        except PositionOutsideTable as e:
            _log_and_ignore(line_number, str(parsed_command), e)
        except UnknownDirection as e:
            _log_and_ignore(line_number, str(parsed_command), e)
    elif parsed_command.command.upper() == "MOVE":
        try:
            robot.move()
        except PositionOutsideTable as e:
            _log_and_ignore(line_number, str(parsed_command), e)
        except RobotNotPlacedYet as e:
            _log_and_ignore(line_number, str(parsed_command), e)
    elif parsed_command.command.upper() == "LEFT":
        try:
            robot.rotate_left()
        except RobotNotPlacedYet as e:
            _log_and_ignore(line_number, str(parsed_command), e)
    elif parsed_command.command.upper() == "RIGHT":
        try:
            robot.rotate_right()
        except RobotNotPlacedYet as e:
            _log_and_ignore(line_number, str(parsed_command), e)
    elif parsed_command.command.upper() == "REPORT":
        try:
            report = robot.report()
        except RobotNotPlacedYet as e:
            _log_and_ignore(line_number, str(parsed_command), e)
    return report


def _log_and_ignore(line_number: int, command: str, message: str) -> None:
    logging.warning(
        f" Command on line {line_number} | {str(command)} | message: {str(message)}"
    )
