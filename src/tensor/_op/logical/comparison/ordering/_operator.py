"""

    *Ordering Comparison*

"""
from abc import ABCMeta

from .._operator import Comparison

__all__ = ["OrderingComparison"]


class OrderingComparison(
    Comparison,
):
    __metaclass__ = ABCMeta
