"""

    *Percentile*

"""
import jax.numpy as jnp

from ._operator import PercentileOperator

__all__ = ["PercentileOperator"]


class Percentile(
    PercentileOperator,
):
    operator = jnp.percentile
