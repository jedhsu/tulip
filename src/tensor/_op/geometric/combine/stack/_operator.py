"""

    *Stack Operator*   S -> Array[T, G]

"""
from abc import ABCMeta

from .._operator import GeometricOperator

__all__ = ["StackOperator"]


class StackOperator(
    GeometricOperator,
):
    __metaclass__ = ABCMeta
