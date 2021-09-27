"""

    *Geometric Operator*   :: Array[T][S] --> Array[T][T]

  Operators mapping on the "extrinsic", i.e. what is not contained.

  This is mostly the geometry of the array. [TODO] confirm

"""
from abc import ABCMeta

from .._operator import ArrayOperator

__all__ = ["GeometricOperator"]


class GeometricOperator(
    ArrayOperator,
):
    __metaclass__ = ABCMeta
