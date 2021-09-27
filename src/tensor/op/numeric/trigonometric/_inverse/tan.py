"""

    *Inverse Tangent*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import InverseTrigonometricOperator

__all__ = ["InverseTangent"]


@dataclass
class InverseTangent(
    InverseTrigonometricOperator,
):
    _operator = jnp.arctan

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(InverseTangent, self).__init__(
            *args,
            **kwargs,
        )
