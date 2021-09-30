use crate::net::tensor;
use model::equiv::Isometrizer;

use spaces::Discrete;

pub trait EqGraph: Graph {
    fn is_representing(
        &self,
        term: &Term,
    ) -> bool;

    fn populate(&self);
}

pub trait Sweep: Graph {
    // fn forward_sweep(&self) -
    fn output(&self) -> Tensor;
}
