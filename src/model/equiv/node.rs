use model::equiv::Isometrizer;

/// check this again!
pub trait EqNode: T
where
    T: Fn<L, R> + Isometrizer,
    L: Symbolic,
    R: FiniteSpace,
{
    fn id(&self) -> L;
    fn children(&self) -> R;
}
