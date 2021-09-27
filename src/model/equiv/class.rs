pub trait EqClass {
    fn is_representating(
        &self,
        term: &Term,
    ) -> bool;
}
