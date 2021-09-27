"""

    *Split*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SplitOperator

__all__ = ["Split"]


@dataclass
class Split(
    SplitOperator,
):
    operator = jnp.split
