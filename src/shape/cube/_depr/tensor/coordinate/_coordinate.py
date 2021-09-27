"""

    *Coordinate*

"""
from dataclasses import dataclass
from typing import Sequence


__all__ = ["Coordinate"]


@dataclass
class Coordinate(
    tuple[int, ...],
):
    def __init__(
        self,
        elements: Sequence[int],
    ):
        super(Coordinate, self).__new__(
            tuple,
            elements,
        )

    @classmethod
    def create(
        cls,
        *element: int,
    ):
        return cls([*element])
