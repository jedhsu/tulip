pub use crate::shape::cube::tensor::TensorTypeParam as TP;

pub trait Associate {
    fn assoc_equiv() -> Vec<Equiv> {
        Equiv::new((TP::X, (TP::Y, TP::Z)), ((TP::X, TP::Y), TP::Z));
    }
}
