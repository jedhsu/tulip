from ._operator import Logarithm
from .bitwise import BitwiseLogarithm
from .denary import DenaryLogarithm
from .natural import NaturalLogarithm


__all__ = [
    "Logarithm",
    "NaturalLogarithm",
    "BitwiseLogarithm",
    "DenaryLogarithm",
    "NaturalLogarithm",
]


# class LogarithmicOperator(TranscendentalOperator):
#     Log1p = jnp.log1p
#     LogAddExp = jnp.logaddexp
#     LogAddExp2 = jnp.logaddexp2
