"""

    *Split Operator*   S -> Array[T, G]

"""
from abc import ABCMeta

from .._operator import GeometricOperator

__all__ = ["SplitOperator"]


class SplitOperator(
    GeometricOperator,
):
    __metaclass__ = ABCMeta
