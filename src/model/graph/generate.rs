pub trait Generate {
    pub type index;

    fn generate(
        ops: Vec<Op>,
        inputs: Vec<Tensor>,
    ) -> Self;

    fn build(
        n: usize,
        index: Fn<Ident, S>,
        inputs: Vec<Tensor>,
    );
}

impl Generate for Substitution {
    fn generate() {}
}
