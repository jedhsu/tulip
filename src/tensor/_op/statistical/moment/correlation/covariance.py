"""

    *Covariance*

"""
import jax.numpy as jnp

from ._operator import CorrelationInference

__all__ = ["Covariance"]


class Covariance(
    CorrelationInference,
):
    fn = jnp.cov

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(Covariance, self).__init__(
            *args,
            **kwargs,
        )
