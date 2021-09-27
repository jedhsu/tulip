"""

    *Negative*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SignOperator

__all__ = ["Negative"]


@dataclass
class Negative(
    SignOperator,
):
    _operator = jnp.negative
