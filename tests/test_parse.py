from os import path

from models.commands.parse import parse_commands_file

from .datatools import COMMANDS_DIRPATH


def test_parse_commands() -> None:
    """Tests parsing commands from a file"""
    file_path = path.join(COMMANDS_DIRPATH, "all_commands.txt")
    parsed_commands = parse_commands_file(file_path)

    assert parsed_commands[0].command == "PLACE"
    assert parsed_commands[0].x == 1
    assert parsed_commands[0].y == 2
    assert parsed_commands[0].direction == "EAST"
    assert parsed_commands[1].command == "MOVE"
    assert parsed_commands[1].x is None
    assert parsed_commands[1].y is None
    assert parsed_commands[1].direction is None
    assert parsed_commands[2].command == "MOVE"
    assert parsed_commands[3].command == "LEFT"
    assert parsed_commands[4].command == "MOVE"
    assert parsed_commands[5].command == "REPORT"
    assert parsed_commands[6].command == "RIGHT"
    assert parsed_commands[7].command == "MOVE"
    assert parsed_commands[8].command == "REPORT"
