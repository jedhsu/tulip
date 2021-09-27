"""

    *Stack*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import StackOperator

__all__ = ["Stack"]


@dataclass
class Stack(
    StackOperator,
):
    operator = jnp.stack
