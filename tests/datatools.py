import json
from os import listdir, path
from typing import List

DATA_FOLDER = path.join(path.dirname(__file__), "data")
COMMANDS_DIRPATH = path.join(DATA_FOLDER, "commands")
EXPECTED_DIRPATH = path.join(DATA_FOLDER, "expected")


TEST_PARAMETERS = [
    (
        path.join(COMMANDS_DIRPATH, x),
        path.join(EXPECTED_DIRPATH, f"{path.splitext(x)[0]}.json"),
    )
    for x in listdir(COMMANDS_DIRPATH)
]


def get_expected_response(file_path: str) -> List[str]:
    with open(file_path) as file:
        return json.load(file)["reports"]
