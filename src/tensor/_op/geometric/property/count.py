"""

    *Count*

"""
import jax.numpy as jnp

from ._operator import GeometricProperty

__all__ = ["Count"]


class Count(
    jnp.size,
    GeometricProperty,
):
    pass
