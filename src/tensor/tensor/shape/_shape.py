"""

    *Shape*

  The shape of a tensor.

  This is the extrinsic geometry, notice how elements are not relevant.

"""
from dataclasses import dataclass
from typing import Sequence

__all__ = ["Shape"]


@dataclass
class Shape(
    tuple[int],
):
    def __init__(
        self,
        sizing: Sequence[int],
    ):
        super(Shape, self).__new__(
            tuple,
            sizing,
        )

    @classmethod
    def create(
        cls,
        *size: int,
    ):
        return cls([*size])

    def __repr__(self) -> str:
        return "[" + " | ".join([str(part) for part in self]) + "]"


class Test:
    @staticmethod
    def vector():
        return Shape.create(5)

    @staticmethod
    def grid():
        return Shape.create(5, 5)

    @staticmethod
    def threetope():
        return Shape.create(5, 5, 5)


class Haha:
    pass
