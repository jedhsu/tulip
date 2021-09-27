"""

    *Equality Comparison*

"""
from abc import ABCMeta

from .._operator import Comparison

__all__ = ["EqualityComparison"]


class EqualityComparison(
    Comparison,
):
    __metaclass__ = ABCMeta
