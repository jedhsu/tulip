"""

    *Quantile*

"""
import jax.numpy as jnp

from ._operator import PercentileOperator

__all__ = ["Quantile"]


class Quantile(
    PercentileOperator,
):
    operator = jnp.quantile
