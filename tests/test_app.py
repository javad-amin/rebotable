import pytest

from app import run_app

from .datatools import TEST_PARAMETERS, get_expected_response


@pytest.mark.parametrize("commands, expected", TEST_PARAMETERS)
def test_app(commands, expected) -> None:
    read_commands = run_app(commands)
    assert read_commands == get_expected_response(expected)
