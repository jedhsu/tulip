"""

    *Fine Topology*

  Inspired from the math definition.

  Generates fully connected layers.

"""
from .._tensor import Tensor
from ..cell import CellIndex
from ._topology import Topology

__all__ = ["FineTopology"]


class FineTopology(
    Topology,
):
    @classmethod
    def link(
        cls,
        tensor: Tensor,
        index: CellIndex,
    ):
        pass
