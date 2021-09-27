"""

    *Median*

"""
import jax.numpy as jnp

from ._operator import PercentileOperator

__all__ = ["Median"]


class Median(
    PercentileOperator,
):
    operator = jnp.median
