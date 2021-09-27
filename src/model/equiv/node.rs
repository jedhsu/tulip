/// check this again!
pub trait EqNode: Fn<X, Y>
where
    A: Symbolic,
    B: FiniteSpace,
{
    fn id(&self) -> A;
    fn children(&self) -> B;
}
