"""

    *Position*

"""
from dataclasses import dataclass

from ..coordinate import CoordinateSystem

__all__ = ["Position"]


@dataclass
class Position:
    # contains a reference to the coordinate system
    _coordinate_system: CoordinateSystem

    def __init__(
        self,
        system: CoordinateSystem,
    ):
        self._coordinate_system = system

    def get_axis_position(
        self,
        ordinal: int,
    ) -> int:
        assert 0 <= ordinal < len(self._coordinate_system.axes), ValueError
        return (
            self._coordinate_system.axes[i] * self._coordinate_system.axes[i].direction
        )

    def get_position(self):
        pass
