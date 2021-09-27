"""

    *Exponential*

"""
from abc import ABCMeta

from .._operator import TranscendentalOperator

__all__ = ["Exponential"]


class Exponential(
    TranscendentalOperator,
):
    __metaclass__ = ABCMeta
