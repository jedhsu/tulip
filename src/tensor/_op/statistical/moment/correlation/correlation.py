"""

    *Correlation*

"""
import jax.numpy as jnp

from ._operator import CorrelationInference

__all__ = ["Correlation"]


class Correlation(
    CorrelationInference,
):
    fn = jnp.cov

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Correlation, self).__init__(
            *args,
            **kwargs,
        )
