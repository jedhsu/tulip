"""

    *Zeros*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import CreationalOperator

__all__ = ["Zeros"]


@dataclass
class Zeros(
    CreationalOperator,
):
    operator = jnp.zeros
