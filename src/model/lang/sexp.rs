pub trait Sexp {
    fn search(&self) -> Vec<Sexp>;
    fn are_all_compatible(exprs: Vec<&Self>) -> bool;
}

pub trait Canonical {
    fn canonize(&self);
    fn decanonize(&self);
}
