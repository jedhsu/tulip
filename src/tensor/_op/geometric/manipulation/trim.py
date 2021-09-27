"""

    *Trim*

  Trim zeros.

"""
import jax.numpy as jnp

from ._operator import Manipulation

__all__ = ["Trim"]


class Trim(
    jnp.trim_zeros,
    Manipulation,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Trim, self).__init__(
            *args,
            **kwargs,
        )
