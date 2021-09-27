"""

    *Tensor,   [Bindings]*

"""
from .index import IndexTensor
from .initialize import Test as InitializeTest
from .move import Move

__all__ = ["Tensor"]


class Tensor(
    Move,
    IndexTensor,
):
    pass


class Test:
    square = Tensor.create(InitializeTest.square)
    square_5x5 = Tensor.create(InitializeTest.square_5x5)
