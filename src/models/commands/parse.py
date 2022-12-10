from typing import List, Literal, Optional

from pydantic import BaseModel


class ParsedCommand(BaseModel):
    command: Literal["PLACE", "MOVE", "LEFT", "RIGHT", "REPORT"]
    x: Optional[int] = None
    y: Optional[int] = None
    direction: Optional[Literal["NORTH", "SOUTH", "WEST", "EAST"]] = None


def parse_commands_file(file_path: str) -> List[ParsedCommand]:
    """Reads the commands file and parses each command"""
    raw_commands = _get_raw_commands(file_path)
    _print_loaded_command(raw_commands)
    return _get_parsed_commands(raw_commands)


def _print_loaded_command(raw_commands: List[str]) -> None:
    print("Input:")
    for raw_command in raw_commands:
        print(raw_command)
    print("")


def _get_parsed_commands(raw_commands: List[str]) -> List[ParsedCommand]:
    """Parse the data for each line and return a list of parsed commands"""
    parsed_commands = []
    for raw_command in raw_commands:
        command_splitted = raw_command.split()
        if not command_splitted:
            continue
        parsed_command = ParsedCommand(command=command_splitted[0].upper())

        if len(command_splitted) > 1:
            x, y, direction = command_splitted[1].split(",")
            parsed_command = ParsedCommand(
                command=command_splitted[0].upper(),
                x=x,
                y=y,
                direction=direction,
            )

        parsed_commands.append(parsed_command)
    return parsed_commands


def _get_raw_commands(file_path) -> List[str]:
    """Reads the command file and splits the lines of commands into a list"""
    with open(file_path) as commands_file:
        raw_commands = commands_file.read().splitlines()
    return raw_commands
