"""

    *Bitwise Logical Operator*

  A bitwise elemental logical operator.

"""
from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["ComputationalOperator"]


class ComputationalOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
