"""

    *Axis*

"""
import jax.numpy as jnp


class Axis:
    NewAxis = jnp.newaxis
    MoveAxis = jnp.moveaxis
    RollAxis = jnp.rollaxis
    SwapAxes = jnp.swapaxes
