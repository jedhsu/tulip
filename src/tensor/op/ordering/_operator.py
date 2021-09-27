"""

    *Bounding Operator*

"""
from abc import ABCMeta

from .._operator import TrigonometricOperator

__all__ = ["HyperbolicOperator"]


class BoundingOperator(
    Operator,
):
    __metaclass__ = ABCMeta
