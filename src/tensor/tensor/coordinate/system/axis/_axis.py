"""

    *Axis*

"""
from dataclasses import dataclass
from typing import Literal

from .orientation import AxisOrientation

__all__ = ["Axis"]


@dataclass
class Axis(
    AxisOrientation,
):
    ordinal: int

    def __init__(
        self,
        ordinal: int,
        origin: int,
        direction: Literal[1, -1],
    ):
        self.ordinal = ordinal
        super(Axis, self).__init__(
            origin,
            direction,
        )

    @classmethod
    def create(
        cls,
        ordinal: int,
        origin: int = 0,
        direction: Literal[1, -1] = 1,
    ):
        return cls(
            ordinal,
            origin,
            direction,
        )
