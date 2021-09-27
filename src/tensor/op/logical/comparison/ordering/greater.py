"""

    *Greater*

"""
import jax.numpy as jnp

from ._operator import OrderingComparison

__all__ = ["Greater"]


class Greater(
    jnp.gt,
    OrderingComparison,
):
    pass
