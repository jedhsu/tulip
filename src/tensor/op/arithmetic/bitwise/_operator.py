"""

    *Bitwise Arithmetic Operator*

"""
from abc import ABCMeta

from .._operator import ArithmeticOperator

__all__ = ["BitwiseArithmeticOperator"]


class BitwiseArithmeticOperator(
    ArithmeticOperator,
):
    __metaclass__ = ABCMeta
