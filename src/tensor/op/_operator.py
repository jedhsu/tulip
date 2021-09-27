"""

    *Array Operator*

  Operate an array.

  Array operators are functors. # [TODO] review theory & confirm

"""
from abc import ABCMeta

__all__ = ["ArrayOperator"]


class ArrayOperator(
    Functor,
):
    __metaclass__ = ABCMeta
