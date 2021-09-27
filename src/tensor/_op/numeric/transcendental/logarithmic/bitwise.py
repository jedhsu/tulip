"""

    *Bitwise Logarithm*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Logarithm

__all__ = ["BitwiseLogarithm"]


@dataclass
class BitwiseLogarithm(
    Logarithm,
):
    operator = jnp.log2
