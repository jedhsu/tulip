"""

    *Squeeze*

"""
import jax.numpy as jnp

from ._operator import ShapingOperator

__all__ = ["Squeeze"]


class Squeeze(
    ShapingOperator,
):
    operator = jnp.squeeze

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Squeeze, self).__init__(
            *args,
            **kwargs,
        )
