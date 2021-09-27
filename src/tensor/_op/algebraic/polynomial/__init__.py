"""

    *Algebraic Operator*

  Operators on polynomial representations.

"""
import jax.numpy as jnp

from .._operator import ArrayOperator

__all__ = ["AlgebraicOperator"]


class AlgebraicOperator(
    ArrayOperator,
):
    # [TODO] clarify
    polyadd = jnp.polyadd
    polysub = jnp.polysub
    polymul = jnp.polymul

    polyder = jnp.polyder
    polyint = jnp.polyint
    polyval = jnp.polyval
