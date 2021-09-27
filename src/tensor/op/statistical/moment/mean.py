"""

    *Mean*

"""
import jax.numpy as jnp

from ._operator import StatisticalInference

__all__ = ["Mean"]


class Mean(
    StatisticalInference,
):
    fn = jnp.mean

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Mean, self).__init__(
            *args,
            **kwargs,
        )
