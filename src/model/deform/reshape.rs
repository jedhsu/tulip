/// A rewrite rule.
pub trait Reshape<L, R>: Equiv<L, R>
where
    L: Compute,
    R: Compute,
{
    fn reshape(&self) -> Self;
    fn volume(&self) -> usize;
}
