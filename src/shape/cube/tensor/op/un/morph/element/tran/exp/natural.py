"""

    *Natural Exponential*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Exponential

__all__ = ["NaturalExponential"]


@dataclass
class NaturalExponential(
    Exponential,
):
    operator = jnp.exp
