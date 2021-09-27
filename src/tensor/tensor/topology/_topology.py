"""

    *Topology*

  Give some comments on topology in lens of category theory.

  Describe the conditions to be an open set.

  Note that you can only use bool, which is what is evaluated to...

  What exactly are these fundamental elements?

  # [TODO] use category theory to prove equivalence.

"""

from abc import ABCMeta
from abc import abstractmethod

from .._tensor import Tensor
from ..cell import Cell
from ..cells import Cells
from ..movement import Movement
from ..movement import MovementPaths

__all__ = ["Topology"]


class Topology:
    __metaclass__ = ABCMeta

    @abstractmethod
    def spawn(
        self,
    ) -> MovementPaths:
        raise NotImplementedError

    @abstractmethod
    def links(
        self,
        tensor: Tensor,
        cell: Cell,
    ) -> Cells:
        movements = []
