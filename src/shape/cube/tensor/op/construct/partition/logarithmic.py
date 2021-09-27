"""

    *Logarithmic-Spaced Create*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SpacedCreate

__all__ = ["LogarithmicSpacedCreate"]


@dataclass
class LogarithmicSpacedCreate(
    SpacedCreate,
):
    operator = jnp.logspace
