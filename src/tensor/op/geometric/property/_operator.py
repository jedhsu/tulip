"""

    *Geometric Property*

  Returns a property of the array's geometry.

"""
from abc import ABCMeta

from .._geometric import GeometricOperator

__all__ = ["GeometricProperty"]


class GeometricProperty(
    GeometricOperator,
):
    __metaclass__ = ABCMeta
