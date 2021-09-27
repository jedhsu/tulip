"""

    *Identity*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import CreationalOperator

__all__ = ["Identity"]


@dataclass
class Identity(
    CreationalOperator,
):
    operator = jnp.eye
