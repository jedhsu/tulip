import jax.numpy as jnp

from ._operator import BooleanOperator

__all__ = ["BooleanAll"]


operator = jnp.all
pub trait BooleanAll: T where T: Operator + Boolean {
}