"""

    *Sine*

"""
import jax.numpy as jnp

from ._operator import TrigonometricOperator

__all__ = ["Sine"]


class Sine(
    jnp.sin,
    TrigonometricOperator,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Sine, self).__init__(
            *args,
            **kwargs,
        )
