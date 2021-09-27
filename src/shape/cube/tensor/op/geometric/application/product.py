"""

    *Product Sum*

  Sum along an axis.

"""
from abc import ABCMeta

from .._operator import ProductOperator

__all__ = ["ProductOperator"]


class Product(
    ProductOperator,
):
    __metaclass__ = ABCMeta
