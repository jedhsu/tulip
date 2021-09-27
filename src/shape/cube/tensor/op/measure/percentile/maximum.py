"""

    *Maximum*

"""

import jax.numpy as jnp

from ._operator import PercentileOperator

__all__ = ["PercentileOperator"]


class Maximum(
    PercentileOperator,
):
    operator = jnp.maximum
