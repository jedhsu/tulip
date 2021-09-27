"""

    *Axis Maximum*

  Maximum along an axis.

"""
from abc import ABCMeta

from .._operator import BoundOperator

__all__ = ["HyperbolicOperator"]


class BoundingOperator(
    Operator,
):
    __metaclass__ = ABCMeta
