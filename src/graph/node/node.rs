use model::equiv::Isometrizer;

/// check this again!
pub trait EqNode<N>: T
where
    T: Fn<L, R> + Isometrizer,
    N: Level,
    L: Symbolic<N>,
    R: FiniteSpace,
{
    pub type eclasses = Vec<C>;

    fn is_representative(term: &Term) {
        &self.eclasses().iter().any().collect();
    }
    fn representation(term: &Term) {
        Constant
    }

    fn ident(&self) -> L;
    fn children(&self) -> R;
}

pub trait ChildlessEqNode {
    fn is_representative(term: &Term) {}
}
