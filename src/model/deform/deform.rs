
/// THis is algo 1, applying multi-pattern rewrite rules.
pub trait Deform {
    fn deform(&self);
}

impl Deform for Computation {
   pub terms: HashSet<SExpr>;
}
