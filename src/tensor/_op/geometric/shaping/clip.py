"""

    *Clip*

"""
import jax.numpy as jnp

from ._operator import ShapingOperator

__all__ = ["Clip"]


class Clip(
    ShapingOperator,
):
    operator = jnp.clip

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Clip, self).__init__(
            *args,
            **kwargs,
        )
