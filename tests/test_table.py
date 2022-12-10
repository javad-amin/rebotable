from models.position import HIQPosition
from models.table import HIQTable


def test_table_dimensions() -> None:
    """Tests that the width and height of the table are set correctly"""
    table = HIQTable(5, 6)

    assert table.width == 5
    assert table.height == 6


def test_table_is_position_on_the_table() -> None:
    """Tests that given a position we can determine if it is on or off the table"""
    table = HIQTable(5, 6)
    position_on_table = HIQPosition(4, 5)
    position_outside_table = HIQPosition(5, 6)
    position_outside_table_on_x_axis = HIQPosition(7, 3)
    position_outside_table_on_y_axis = HIQPosition(3, 7)
    position_outside_table_negative = HIQPosition(-1, -2)

    assert table.is_on_table(position_on_table) is True
    assert table.is_on_table(position_outside_table) is False
    assert table.is_on_table(position_outside_table_on_x_axis) is False
    assert table.is_on_table(position_outside_table_on_y_axis) is False
    assert table.is_on_table(position_outside_table_negative) is False
