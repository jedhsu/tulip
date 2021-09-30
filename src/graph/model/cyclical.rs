pub trait Cyclical {
    fn is_acyclic(&self);
}
pub trait Complexity {
    fn complexity(&self);
}

pub trait CheckCyling {
    fn will_cause_cycles(&self) -> bool;
    fn checking_complexity(&self) -> Degree;
}
