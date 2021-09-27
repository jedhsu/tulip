from ._operator import Exponential
from .bitwise import BitwiseExponential
from .natural import NaturalExponential

__all__ = [
    "Exponential",
    "BitwiseExponential",
    "NaturalExponential",
]

# class ExponentialOperator(TranscendentalOperator):
#     Exp = jnp.exp
#     Exp2 = jnp.exp2  # [TODO] clarify what this is

#     ExpM1 = jnp.expm1

#     LdExp = jnp.ldexp  # [TODO] clarify
#     FrExp = jnp.frexp
