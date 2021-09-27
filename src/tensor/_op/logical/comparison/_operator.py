"""

    *Comparison*

"""
from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["Comparison"]


class Comparison(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
