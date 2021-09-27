"""

    *Linear-Spaced Create*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SpacedCreate

__all__ = ["LinearSpacedCreate"]


@dataclass
class LinearSpacedCreate(
    SpacedCreate,
):
    operator = jnp.linspace
