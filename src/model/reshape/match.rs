pub trait Match<Fn<L, R>> where R: Fn<Var<L>, Subterm<e>>
    pub type Matches;

    fn apply(&self, r::Density) ;
}
