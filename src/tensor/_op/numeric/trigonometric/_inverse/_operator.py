"""

    *Inverse Trigonometric Operator*

"""
from abc import ABCMeta

from .._operator import TrigonometricOperator

__all__ = ["InverseTrigonometricOperator"]


class InverseTrigonometricOperator(
    TrigonometricOperator,
):
    __metaclass__ = ABCMeta
