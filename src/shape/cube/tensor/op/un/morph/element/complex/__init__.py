"""

    *Complex Operator*   :: Array[Complex] --> Array[Property[Complex]]

  Operators that return a property of a complex number.

"""
import jax.numpy as jnp

from ._numeric import NumericOperator


class ComplexOperator(NumericOperator):
    Real = jnp.real
    Imaginary = jnp.imag
    Angle = jnp.angle  # angle of complex argument

    Conjugate = jnp.conj  # jnp.conjugate is alias
