"""

    *Vertical Stack*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import StackOperator

__all__ = ["VerticalStack"]


@dataclass
class VerticalStack(
    StackOperator,
):
    operator = jnp.vstack
