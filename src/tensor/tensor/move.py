"""

    *Tensor,   [Move Interface]*

  Modify the index of the array under a fixed coordinate system.

"""
from .cell import Cell
from .index import IndexTensor
from .index import Test as IndexTensorTest
from .movement import MovementPath
from .shape import Shape

__all__ = ["Move"]


class Move(
    IndexTensor,
):
    def jump(
        self,
        *coordinate: int,
    ) -> Cell:
        assert len([*coordinate]) == len(self._tensor._tensor.shape), ValueError
        index = self.focus.index.add(
            MovementPath.create(*coordinate),
            shape=Shape(self._tensor._tensor.shape),
        )
        self.focused = self[index.coordinate]
        return self[index.coordinate]

    def step(
        self,
        dimension: int,
        amount: int,
    ):
        """
        Only move a single dimension.
        """
        movement = [0] * self._tensor._tensor.shape
        movement[dimension] = amount
        return self.jump(*movement)
