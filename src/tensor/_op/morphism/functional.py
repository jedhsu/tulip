import jax.numpy as jnp

from .base import ArrayTransform


class FunctionalTransform(ArrayTransform):
    """
    Functional transforms.

    """

    Heaviside = jnp.heaviside  # [TODO] does ths really go here??

    ModifiedBessel0 = jnp.i0
