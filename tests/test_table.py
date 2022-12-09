from position import Position
from table import Table


def test_table_dimensions() -> None:
    table = Table(5, 6)

    assert table.width == 5
    assert table.height == 6


def test_table_is_position_on_the_table() -> None:
    table = Table(5, 6)
    position_on_table = Position(4, 5)
    position_outside_table = Position(5, 6)
    position_outside_table_negative = Position(-1, -2)

    assert table.is_on_table(position_on_table) == True
    assert table.is_on_table(position_outside_table) == False
    assert table.is_on_table(position_outside_table_negative) == False
