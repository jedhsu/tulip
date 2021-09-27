"""

    *Horizontal Split*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SplitOperator

__all__ = ["HorizontalSplit"]


@dataclass
class HorizontalSplit(
    SplitOperator,
):
    operator = jnp.hsplit
