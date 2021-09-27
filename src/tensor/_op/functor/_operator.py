"""

    *Functor*   :: Array[S] --> Array[T]

  Operators which return a different containing type.

"""
from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["TranscendentalOperator"]


class TranscendentalOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
