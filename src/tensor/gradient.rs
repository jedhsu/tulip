pub trait Grad<X, Y>
where
    X: Fn + Tensor,
    Y: Fn + Tensor,
{
    pub type Value;

    /// TODO argums cases
    fn grad(&self, argidx: usize) -> Value;
    fn evaluate(&self, argidx: usize) -> Value;
}

pub trait FiniteDifference {
    fn is_within(&self, epsilon: f64) -> bool;
}

pub trait Jacobian {
    fn 
}