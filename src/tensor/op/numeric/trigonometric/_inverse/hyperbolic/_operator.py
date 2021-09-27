"""

    *Inverse Hyperbolic Operator*

"""
from abc import ABCMeta

from .._operator import TrigonometricOperator

__all__ = ["InverseHyperbolicOperator"]


class HyperbolicOperator(
    TrigonometricOperator,
    InverseOperator,
):
    __metaclass__ = ABCMeta
