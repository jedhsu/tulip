"""

    *Manipulation*

  Functional manipulation.

"""
from abc import ABCMeta

from .._operator import GeometricOperator

__all__ = ["Manipulation"]


class Manipulation(
    GeometricOperator,
):
    __metaclass__ = ABCMeta
