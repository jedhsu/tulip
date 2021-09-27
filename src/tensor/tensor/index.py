"""

    *Tensor,   [Index Interface]*

"""
from dataclasses import dataclass
from itertools import product
from typing import Sequence

from ._tensor import Tensor
from .cell import Cell
from .cell import CellIndex
from .initialize import Test as InitializeTest

__all__ = ["IndexTensor"]


@dataclass
class IndexTensor:
    _tensor: Tensor
    cells: dict[CellIndex, Cell]
    focus: Cell

    @classmethod
    def create(
        cls,
        tensor: Tensor,
    ):
        cells = {
            CellIndex(*idx): Cell(
                tensor,
                CellIndex(*idx),
                None,
            )
            for idx in product(*[range(dim) for dim in tensor._tensor.shape])
        }
        focus = [0] * len(tensor._tensor.shape)
        focused = cells[CellIndex(*focus)]
        return cls(
            tensor,
            cells,
            focused,
        )

    def __getitem__(
        self,
        index: Sequence[int],
    ) -> Cell:
        return self.cells[CellIndex(*index)]


class Test:
    square = IndexTensor.create(InitializeTest.square)
    square_5x5 = IndexTensor.create(InitializeTest.square_5x5)
