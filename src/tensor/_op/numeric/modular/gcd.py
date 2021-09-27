"""

    *Gcd*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import ModularArithmetic

__all__ = ["Gcd"]


@dataclass
class Gcd(
    ModularArithmetic,
):
    _operator = jnp.gcd
