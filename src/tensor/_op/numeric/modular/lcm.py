"""

    *Lcm*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import ModularArithmetic

__all__ = ["Lcm"]


@dataclass
class Lcm(
    ModularArithmetic,
):
    _operator = jnp.lcm
