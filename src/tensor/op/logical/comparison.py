"""

    *Comparison Operator*

"""

import jax.numpy as jnp

from ._operator import ArrayOperator


class ComparisonOperator(ArrayOperator):
    """
    Element-wise comparison operators.

    """

    Equal = jnp.equal
    NotEqual = jnp.not_equal

    IsClose = jnp.isclose

    GreaterThan = jnp.greater
    GreaterEqualThan = jnp.greater_equal

    LesserThan = jnp.less
    LesserEqualThan = jnp.less_equal

    Where = jnp.where  # predicate evaluation
    Condition = jnp.extract  # #[TODO] also predicate eval? compare

    # [TODO] arity note?
    allclose = jnp.allclose  # element-wise equality within tolerance
