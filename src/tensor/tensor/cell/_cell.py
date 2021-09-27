"""

    *Cell*

  A tensor cell at a coordinate.

"""

from typing import Any

from dataclasses import dataclass

from .._tensor import Tensor
from .position import Position
from .index import CellIndex

__all__ = ["Cell"]


@dataclass
class Cell(
    Position,
):
    # reference to Tensor
    tensor: Tensor
    index: CellIndex
    content: Any

    def __init__(
        self,
        tensor: Tensor,
        index: CellIndex,
        content: Any,
    ):
        self.tensor = tensor
        self.index = index
        self.content = content
        super(Cell, self).__init__(
            tensor.coordinate_system,
        )
