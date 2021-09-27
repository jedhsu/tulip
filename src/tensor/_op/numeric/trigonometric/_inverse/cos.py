"""

    *Inverse Cosine*

"""
from dataclasses import dataclass

import jax.numpy as jnp

from ._operator import InverseTrigonometricOperator

__all__ = ["InverseCosine"]


@dataclass
class InverseCosine(
    InverseTrigonometricOperator,
):
    _operator = jnp.arccos

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super(InverseCosine, self).__init__(
            *args,
            **kwargs,
        )
