import jax.numpy as jnp

from ._operator import StatisticalOperator


class CorrelationOperator(StatisticalOperator):
    CorrelationCoefficients = jnp.corrcoef
    Correlate = jnp.correlate
