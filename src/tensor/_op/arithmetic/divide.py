"""

    *Element Divide*

"""
import jax.numpy as jnp

__all__ = ["ElementDivide"]


class ElementDivide(
    ElementOperator,
    BinaryOperator,
    ArrayOperator,
):
    fn: ClassVar = jnp.divide
