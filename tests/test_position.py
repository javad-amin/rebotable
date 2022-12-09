from position import Position


def test_position() -> None:
    """Tests that the x and y axis of a position are correctly set"""
    position = Position(0, 0)

    assert position.x == 0
    assert position.y == 0


def test_add_positions() -> None:
    """Tests that two positions/points can be added together, useful for movement"""
    position_1 = Position(2, 3)
    position_2 = Position(1, 1)

    assert position_1 + position_2 == Position(3, 4)


def test_string_representation_of_a_position() -> None:
    """Tests that the string representation of a position is as desireable"""
    position = Position(2, 3)

    assert str(position) == "2,3"
