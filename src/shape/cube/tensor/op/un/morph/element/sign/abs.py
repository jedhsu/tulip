"""

    *Absolute*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SignOperator

__all__ = ["Absolute"]


@dataclass
class Absolute(
    SignOperator,
):
    _operator = jnp.abs
