pub use crate::shape::cube::tensor::TensorTypeParam as TP;

pub trait Commute {
    fn commut_equiv() -> Vec<Equiv> {
        Equiv::new((TP::X, TP::Y), (TP::Y, TP::X));
    }
}
