pub trait Symbolic {
    pub type Symbol;
}

pub trait TensorOperator: Symbolic {
    pub type TensorOp;
}
