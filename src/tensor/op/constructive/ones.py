"""

    *Ones*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import CreationalOperator

__all__ = ["Ones"]


@dataclass
class Ones(
    CreationalOperator,
):
    operator = jnp.ones
