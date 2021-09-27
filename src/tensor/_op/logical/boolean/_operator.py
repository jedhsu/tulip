"""

    *Boolean Operator*

  Might call this predicate instead.

"""
from abc import ABCMeta

from .._operator import LogicalOperator

__all__ = ["BooleanOperator"]


class BooleanOperator(
    LogicalOperator,
):
    __metaclass__ = ABCMeta
