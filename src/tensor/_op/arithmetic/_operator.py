"""

    *Arithmetic Operator*

"""
from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["ArithmeticOperator"]


class ArithmeticOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
