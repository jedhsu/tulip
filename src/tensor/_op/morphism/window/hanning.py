"""

    *Hanning Window*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Window

__all__ = ["HanningWindow"]


@dataclass
class HanningWindow(
    Window,
):
    operator = jnp.hanning
