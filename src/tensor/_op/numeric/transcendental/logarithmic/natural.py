"""

    *Natural Logarithm*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Logarithm

__all__ = ["NaturalLogarithm"]


@dataclass
class NaturalLogarithm(
    Logarithm,
):
    operator = jnp.log
