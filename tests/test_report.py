def report(command: str) -> str:
    return f"The {command=} not accepted! First acceptable command is PLACE <x_position>,<y_position>,<direction>"


def test_report_robot_not_placed_yet():
    command = "REPORT"
    assert (
        report(command)
        == f"The {command=} not accepted! First acceptable command is PLACE <x_position>,<y_position>,<direction>"
    )
