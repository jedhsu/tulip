"""

    *Tensor,   [Initialize Interface]*

"""
import numpy as np

from ._tensor import Tensor
from .coordinate import CoordinateSystem

__all__ = ["InitializeTensor"]


class InitializeTensor(
    Tensor,
):
    def __init__(
        self,
        _tensor: np.ndarray,
        coordinate_system: CoordinateSystem,
    ):
        super(InitializeTensor, self).__init__(
            _tensor,
            coordinate_system,
        )

    @classmethod
    def create(
        cls,
        *args,
        **kwargs,
    ):
        _tensor = np.array(
            *args,
            **kwargs,
        )
        coordinate_system = CoordinateSystem(dimensions=len(_tensor.shape))
        return cls(
            _tensor,
            coordinate_system,
        )


# [TODO] extend to pixel case


class Test:
    square = InitializeTensor.create(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    )

    square_5x5 = InitializeTensor.create(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]
    )
