"""

    *Pad*

"""
import jax.numpy as jnp

from ._operator import Manipulation

__all__ = ["Pad"]


class Pad(
    Manipulation,
):
    operator = jnp.pad

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Pad, self).__init__(
            *args,
            **kwargs,
        )
