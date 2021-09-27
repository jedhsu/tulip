"""

    *Hyperbolic Sine*

"""
import jax.numpy as jnp

from ._operator import HyperbolicOperator

__all__ = ["HyperbolicSine"]


class HyperbolicSine(
    jnp.cos,
    HyperbolicOperator,
):
    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(HyperbolicSine, self).__init__(
            *args,
            **kwargs,
        )
