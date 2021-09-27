"""

    *HyperbolicCosine*

"""
import jax.numpy as jnp

from ._operator import TrigonometricOperator

__all__ = ["HyperbolicCosine"]


class HyperbolicCosine(
    jnp.cosh,
    TrigonometricOperator,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(HyperbolicCosine, self).__init__(
            *args,
            **kwargs,
        )
