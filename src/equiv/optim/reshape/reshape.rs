pub trait Complexity {
    fn complexity(&self);
}

pub trait CheckCyling {
    fn will_cause_cycles(&self) -> bool;
    fn checking_complexity(&self) -> Degree;
}

/// A rewrite rule.
pub trait Reshape<L, R>: X
where
    X: Equiv<L, R>,

    L: Compute,
    R: Compute,
{
    pub type Complexor: Complexity;

    fn reshape(&self) -> Self;

    fn volume(&self) -> usize;

    fn apply(
        &self,
        input: &Graph,
        shaping: Shaping,
    ) -> Graph;
}
