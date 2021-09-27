"""

    *Positive*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SignOperator

__all__ = ["Positive"]


@dataclass
class Positive(
    SignOperator,
):
    _operator = jnp.positive
