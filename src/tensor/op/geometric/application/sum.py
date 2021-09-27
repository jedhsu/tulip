"""

    *Axis Sum*

  Sum along an axis.

"""
from abc import ABCMeta

from .._operator import AxisOperator

__all__ = ["Sum"]


class Sum(
    AxisOperator,
):
    __metaclass__ = ABCMeta
