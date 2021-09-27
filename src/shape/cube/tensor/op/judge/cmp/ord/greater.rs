"""

    *Greater*

"""
import jax.numpy as jnp

from ._operator import OrderingComparison

__all__ = ["Greater"]

pub trait Greater {
    fn scalar_greater();
    fn element_greater();
    fn object_greater();
}

impl ElementGreater (
    jnp.gt,
    OrderingComparison,
):
    pass
