class AxisOp:
    sum = jnp.sum
    Trace = jnp.trace  # [TODO] clarify  # sum along diagonals

    cumsum = jnp.cumsum

    average = jnp.average  # average along axis
    max = jnp.max  # max along axis
    min = jnp.min

    prod = jnp.prod
    cumprod = jnp.cumprod
    cumproduct = jnp.cumproduct  # [TODO] how different?
