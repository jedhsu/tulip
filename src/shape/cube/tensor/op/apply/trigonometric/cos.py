"""

    *Cosine*

"""
import jax.numpy as jnp

from ._operator import TrigonometricOperator

__all__ = ["Cosine"]


class Cosine(
    jnp.cos,
    TrigonometricOperator,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Cosine, self).__init__(
            *args,
            **kwargs,
        )
