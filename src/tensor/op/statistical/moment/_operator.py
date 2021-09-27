"""

    *Moment Inferece*

  Operators inferring distribution moments.

"""
from abc import ABCMeta

from .._operator import StatisticalInference

__all__ = ["MomentInference"]


class MomentInference(
    StatisticalInference,
):
    __metaclass__ = ABCMeta
