"""

    *Standard Deviation*

"""
import jax.numpy as jnp

from ._operator import VarianceInference

__all__ = ["StandardDeviation"]


class StandardDeviation(
    VarianceInference,
):
    fn = jnp.std

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(StandardDeviation, self).__init__(
            *args,
            **kwargs,
        )
