"""

    *Cells*

"""
from dataclasses import dataclass
from typing import Mapping
from typing import Optional
from typing import Sequence

from ..cell import Cell
from ..index import CellIndex

__all__ = ["Cells"]


@dataclass
class Cells(
    dict[CellIndex, Cell],
):
    name: Optional[str]

    def __init__(
        self,
        dct: Mapping[CellIndex, Cell],
        name: Optional[str] = None,
    ):
        self.name = name
        super(Cells, self).__init__(dct)

    @classmethod
    def from_list(
        cls,
        lst: Sequence[Cell],
        name: Optional[str],
    ):
        return cls(
            {el.index: el for el in lst},
            name,
        )
