pub trait EqNode<A, B>
where
    A: Symbolic,
    B: FiniteSpace,
{
    fn id(&self) -> A;
    fn children(&self) -> B;
}
