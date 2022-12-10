from os import path
from typing import List

from models.commands.parse import parse_commands_file
from models.commands.router import route_command
from models.robot import HIQRobot

CURRENT_FOLDER = path.join(path.dirname(__file__))


def run_app(file_path: str) -> List[str]:
    """Main app that parses the commands file and runs them"""
    parsed_commands = parse_commands_file(file_path)

    robot = HIQRobot()
    reports = []
    for line_number, parsed_command in enumerate(parsed_commands):
        if report := route_command(line_number, parsed_command, robot):
            reports.append(report)
    return reports


if __name__ == "__main__":
    default_example = path.join(CURRENT_FOLDER, "examples/commands.txt")
    command_file_path = (
        input(
            f"Provide the path to your command file or use default file ({default_example})\n"
        )
        or default_example
    )

    app_response = run_app(command_file_path)
    print("\nOutput:")
    for response in app_response:
        print(response)
