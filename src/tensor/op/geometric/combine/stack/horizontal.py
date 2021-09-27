"""

    *Horizontal Stack*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import StackOperator

__all__ = ["HorizontalStack"]


@dataclass
class HorizontalStack(
    StackOperator,
):
    operator = jnp.hstack
