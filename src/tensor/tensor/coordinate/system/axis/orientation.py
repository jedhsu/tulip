"""

    *Orientation*

"""
from dataclasses import dataclass
from typing import Literal

__all__ = ["AxisOrientation"]


@dataclass
class AxisOrientation:
    origin: int
    direction: Literal[1, -1]

    def orient(
        self,
        origin: int,
        direction: Literal[1, -1],
    ):
        self.origin = origin
        self.direction = direction
