"""

    *Blackman Window*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Window

__all__ = ["BlackmanWindow"]


@dataclass
class BlackmanWindow(
    Window,
):
    operator = jnp.blackman
