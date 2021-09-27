"""

    *Percentile Operator*

  Percentile statistical operators.

"""
from abc import ABCMeta

from .._operator import StatisticalInference

__all__ = ["PercentileOperator"]


class PercentileOperator(
    StatisticalInference,
):
    __metaclass__ = ABCMeta
