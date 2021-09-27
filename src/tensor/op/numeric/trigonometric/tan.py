"""

    *Tangent*

"""
import jax.numpy as jnp

from ._operator import TrigonometricOperator

__all__ = ["Tangent"]


class Tangent(
    jnp.tan,
    TrigonometricOperator,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Tangent, self).__init__(
            *args,
            **kwargs,
        )
