"""

    *Select*

"""
import jax.numpy as jnp

from ._operator import Manipulation

__all__ = ["Select"]


class Select(
    jnp.select,
    Manipulation,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Select, self).__init__(
            *args,
            **kwargs,
        )
