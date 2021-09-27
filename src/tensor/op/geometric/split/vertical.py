"""

    *Vertical Split*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SplitOperator

__all__ = ["VerticalSplit"]


@dataclass
class VerticalSplit(
    SplitOperator,
):
    operator = jnp.vsplit
