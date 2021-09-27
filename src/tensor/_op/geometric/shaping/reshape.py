"""

    *Reshape*

"""
import jax.numpy as jnp

from ._operator import ShapingOperator

__all__ = ["Reshape"]


class Reshape(
    ShapingOperator,
):
    operator = jnp.reshape

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Reshape, self).__init__(
            *args,
            **kwargs,
        )
