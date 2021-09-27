"""

    *Statistical Inference*

  Operators performing statistical inference.

"""
from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["StatisticalInference"]


class StatisticalInference(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
