"""

    *Chess Topology*

  Alternating topology.

"""
from .._tensor import Tensor
from ..cell import CellIndex
from ..cells import Cells
from ..movement import Movement
from ..movement import MovementPaths
from ._topology import Topology

__all__ = ["ChessTopology"]


class ChessTopology(
    Topology,
):
    def spawn(self):
        return [
            MovementPaths(
                (-1,),
                (+1,),
            ),
        ]
