"""

    *Spaced Create*

  Constructors based on element-wise difference equation.

"""
from abc import ABCMeta

from .._operator import Create

__all__ = ["SpacedCreate"]


class SpacedCreate(
    Create,
):
    __metaclass__ = ABCMeta
