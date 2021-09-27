"""

    *Repeat*

"""
import jax.numpy as jnp

from ._operator import Manipulation

__all__ = ["Pad"]


class Repeat(
    jnp.repeat,
    Manipulation,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Repeat, self).__init__(
            *args,
            **kwargs,
        )
