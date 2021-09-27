"""

    *Logarithm*

"""
from abc import ABCMeta

from .._operator import TranscendentalOperator

__all__ = ["Logarithm"]


class Logarithm(
    TranscendentalOperator,
):
    __metaclass__ = ABCMeta
