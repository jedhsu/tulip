"""

    *Element Multiply*

"""
from ._operator import ArithmeticOperator

__all__ = ["ElementMultiply"]


class ElementMultiply(
    ElementOperator,
    BinaryOperator,
    ArrayOperator,
):

    func = jnp.multiply
