"""

    *Coordinate System*

"""
from dataclasses import dataclass
from typing import Literal
from typing import Sequence

from .axis import Axis

__all__ = ["CoordinateSystem"]


@dataclass
class CoordinateSystem:
    axes: Sequence[Axis]

    def __init__(
        self,
        *,
        dimensions: int,
    ):
        self.axes = [Axis.create(size) for size in range(dimensions)]

    def orient(
        self,
        orients: Sequence[tuple[int, Literal[1, -1]]],
    ):
        assert len(self.axes) == len(orients)
        for axis, ori in zip(self.axes, orients):
            axis.orient(*ori)
