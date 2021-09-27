"""

    *Inverse Sine*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import InverseTrigonometricOperator

__all__ = ["InverseSine"]


@dataclass
class InverseSine(
    InverseTrigonometricOperator,
):
    _operator = jnp.arcsin

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(InverseSine, self).__init__(
            *args,
            **kwargs,
        )
