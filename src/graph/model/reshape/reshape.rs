/// A rewrite rule.
///
/// States semantic equivalence of L & R.
pub trait Reshape<L, R>: X
where
    X: Equiv<L, R>,

    L: Pattern,
    R: Pattern,
{
    pub type Complexor: Complexity;

    fn reshape(&self) -> &Self;

    fn volume(&self) -> u64;

    fn apply(
        &self,
        c: Term,
        input: &Graph,
        shaping: Shaping,
    ) -> Graph;
}
