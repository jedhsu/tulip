"""

    *Transcendental Operator*   :: Array[Number] -> Array[TranscendentalNumber]

  Operators which return transcendental (non-algebraic) numbers,

"""
from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["TranscendentalOperator"]


class TranscendentalOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
