"""

    *Diagonal Split*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SplitOperator

__all__ = ["DiagonalSplit"]


@dataclass
class DiagonalSplit(
    SplitOperator,
):
    operator = jnp.dsplit
