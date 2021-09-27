"""

    *Diagonal Stack*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import StackOperator

__all__ = ["DiagonalStack"]


@dataclass
class DiagonalStack(
    StackOperator,
):
    operator = jnp.dstack
