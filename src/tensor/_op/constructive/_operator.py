"""

    *Create*   S -> Array[T, G]

  Operators that instantiate objects of the type.

"""
import jax.numpy as jnp

from .._operator import ArrayOperator

# [TODO] typing can get much tighter


class Create(ArrayOperator):
    # low-level constructor
    Array = jnp.ndarray

    Zeros = jnp.zeros
    Ones = jnp.ones

    Empty = jnp.empty
    Full = jnp.full

    # TODO: IDEALLY want Fn[N, Array[Dtype][N]]
    # arange: Callable[[N],
    Range = jnp.arange

    Tile = jnp.tile

    Eye = jnp.eye

    Identity = jnp.identity
