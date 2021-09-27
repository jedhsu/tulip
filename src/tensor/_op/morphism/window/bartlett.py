"""

    *Bartlett Window*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Window

__all__ = ["BartlettWindow"]


@dataclass
class BartlettWindow(
    Window,
):
    operator = jnp.bartlett
