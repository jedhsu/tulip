"""

    *Variance Inference*

"""
from abc import ABCMeta

from .._operator import MomentInference

__all__ = ["VarianceInference"]


class VarianceInference(
    MomentInference,
):
    __metaclass__ = ABCMeta
