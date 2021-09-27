"""

    *Roll*

"""
import jax.numpy as jnp

from ._operator import ShapingOperator

__all__ = ["Roll"]


class Roll(
    ShapingOperator,
):
    operator = jnp.roll

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Roll, self).__init__(
            *args,
            **kwargs,
        )
