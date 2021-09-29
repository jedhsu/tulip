pub struct Add {}

pub trait Add: X
where
    X: TensorOp + BinOp<Tensor, Tensor> + P,
    P: Associativity + Commutativity,
{
}

pub trait Commutativity {
    fn commut_equiv() -> Vec<Equiv> {
        Equiv::new(
            (TensorType::X, (TensorType::Y, TensorType::Z)),
            ((TensorType::X, TensorType::Y), TensorType::Z),
        );
    }
}
