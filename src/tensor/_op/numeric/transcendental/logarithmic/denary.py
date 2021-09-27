"""

    *Denary Logarithm*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Logarithm

__all__ = ["DenaryLogarithm"]


@dataclass
class DenaryLogarithm(
    Logarithm,
):
    operator = jnp.log10
