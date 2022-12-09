from dataclasses import dataclass

from position import Position


@dataclass
class Robot:
    position: Position = Position(-1, -1)
    direction: str = "North"
