"""

    *Movement Path*

  An exact movement.

"""
from dataclasses import dataclass
from typing import Sequence

__all__ = ["MovementPath"]


@dataclass
class MovementPath(
    tuple[int],
):
    def __init__(
        self,
        values: Sequence[int],
    ):
        super(MovementPath, self).__new__(
            tuple,
            values,
        )

    @classmethod
    def create(
        cls,
        *value: int,
    ):
        return cls([*value])

    def __hash__(self) -> int:
        # [TODO] this needs work
        return int("".join([str(i) + str(el) for i, el in enumerate(self)]))
