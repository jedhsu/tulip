"""

    *Take*

"""
import jax.numpy as jnp

from ._operator import Manipulation

__all__ = ["Take"]


class Take(
    jnp.take,
    Manipulation,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Take, self).__init__(
            *args,
            **kwargs,
        )
