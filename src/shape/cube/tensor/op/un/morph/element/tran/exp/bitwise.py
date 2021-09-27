"""

    *Bitwise Exponential*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Exponential

__all__ = ["BitwiseExponential"]


@dataclass
class BitwiseExponential(
    Exponential,
):
    operator = jnp.exp2
