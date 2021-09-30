use sexp::Sexp as Term;

pub trait Expr: Term {
    pub type Subterm;

    fn search(&self) -> Vec<Expr>;
    fn are_all_compatible(exprs: Vec<&Self>) -> bool;
    fn awaiting_replacement(&self) -> Self::Subterm;
}
