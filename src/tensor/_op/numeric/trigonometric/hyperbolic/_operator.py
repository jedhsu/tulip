"""

    *Hyperbolic Operator*

"""
from abc import ABCMeta

from .._operator import TrigonometricOperator

__all__ = ["HyperbolicOperator"]


class HyperbolicOperator(
    TrigonometricOperator,
):
    __metaclass__ = ABCMeta
