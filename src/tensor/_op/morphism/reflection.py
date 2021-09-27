import jax.numpy as jnp

from .base import ArrayTransform


class Reflection(ArrayTransform):
    flip = jnp.flip  # flip along axis
