"""

    *Shaping Operator*

"""
from abc import ABCMeta

from .._operator import GeometricOperator

__all__ = ["ShapingOperator"]


class ShapingOperator(
    GeometricOperator,
):
    __metaclass__ = ABCMeta
