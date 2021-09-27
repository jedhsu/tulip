"""

    *Transpose*

"""
import jax.numpy as jnp

from ._operator import ShapingOperator

__all__ = ["Transpose"]


class Transpose(
    ShapingOperator,
):
    operator = jnp.transpose

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Transpose, self).__init__(
            *args,
            **kwargs,
        )
