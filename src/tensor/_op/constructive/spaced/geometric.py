"""

    *Geometric-Spaced Create*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import SpacedCreate

__all__ = ["GeometricSpacedCreate"]


@dataclass
class GeometricSpacedCreate(
    SpacedCreate,
):
    operator = jnp.geomspace
