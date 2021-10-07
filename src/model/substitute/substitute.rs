/// A graph substitution. Applies a reshape.
pub struct Reshape {
    left: Graph,
    right: Graph,
}

pub trait Tensor<Ident, Cfg, Shape> {}
