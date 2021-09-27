"""

    *Hamming Window*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Window

__all__ = ["HammingWindow"]


@dataclass
class HammingWindow(
    Window,
):
    operator = jnp.hamming
