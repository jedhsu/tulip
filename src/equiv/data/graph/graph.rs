use model::equiv::Isometrizer;

use spaces::Discrete;

pub trait EqGraph: Graph {
    fn is_representing(
        &self,
        term: &Term,
    ) -> bool;

    fn populate(&self);
    fn sweep(&self);
}
