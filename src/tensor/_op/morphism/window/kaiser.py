"""

    *Kaiser Window*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import Window

__all__ = ["KaiserWindow"]


@dataclass
class KaiserWindow(
    Window,
):
    operator = jnp.kaiser
