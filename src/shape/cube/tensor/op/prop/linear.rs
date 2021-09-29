pub use crate::shape::cube::tensor::TensorTypeParam as TP;

pub trait Linear {
    fn linear_equiv() -> Vec<Equiv> {
        Equiv::new((TP::X, TP::Y), (TP::Y, TP::X));
    }
}
