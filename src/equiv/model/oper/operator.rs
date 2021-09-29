pub trait TensorOperator: X
where
    X: Op<Tensor, Tensor>,
    Param: A + B,
{
}
