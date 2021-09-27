"""

    *Variance*

"""
import jax.numpy as jnp

from ._operator import VarianceInference

__all__ = ["Variance"]


class Variance(
    VarianceInference,
):
    fn = jnp.var

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Variance, self).__init__(
            *args,
            **kwargs,
        )
