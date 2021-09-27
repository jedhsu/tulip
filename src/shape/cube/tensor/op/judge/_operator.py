"""

    *Logical Operator*

  Might call this predicate instead.

"""
from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["LogicalOperator"]


class LogicalOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
