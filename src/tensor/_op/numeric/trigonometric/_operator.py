"""

    *Trigonometric Operator*   :: Array[Angle] --> Array[Number]

  Operators that map angles to numbers.

"""
from abc import ABCMeta

from .._operator import NumericOperator

__all__ = ["TrigonometricOperator"]


class TrigonometricOperator(
    NumericOperator,
    metaclass=ABCMeta,
):
    pass
