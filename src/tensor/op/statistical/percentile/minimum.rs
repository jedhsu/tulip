pub trait Minimum: Percentile + Fn<X, Y> where X: Tensor, Y: Tensor{
    operator = jnp.minimum
}