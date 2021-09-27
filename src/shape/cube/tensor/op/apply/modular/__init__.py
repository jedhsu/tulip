"""

Modular arithmetic operators.

"""
import jax.numpy as jnp

from .base import NumericOperator


# [TODO] think about the typing interfaces!
# [TODO] subtype on arity pattern
class ModularArithmeticOperator(NumericOperator):

    mod = jnp.mod

    gcd = jnp.gcd
    lcm = jnp.lcm

    divmod = jnp.divmod

    Modf = jnp.modf
    FMod = jnp.fmod
