"""

    *Window*

  Frequency / window / fft operators.

"""
from abc import ABCMeta

from .._operator import TensorMorphism

__all__ = ["Window"]


class Window(
    TensorMorphism,
):
    __metaclass__ = ABCMeta
