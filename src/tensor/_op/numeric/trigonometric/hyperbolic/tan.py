"""

    *HyperbolicTangent*

"""
import jax.numpy as jnp

from ._operator import HyperbolicOperator

__all__ = ["HyperbolicTangent"]


class HyperbolicTangent(
    jnp.cosh,
    HyperbolicOperator,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(HyperbolicTangent, self).__init__(
            *args,
            **kwargs,
        )
