from dataclasses import dataclass

from models.position import Position


@dataclass
class HIQTable:
    width: int = 0
    height: int = 0

    def is_on_table(self, position: Position) -> bool:
        if all(
            [
                0 <= position.x < self.width,
                0 <= position.y < self.height,
            ]
        ):
            return True
        return False
