use model::equiv::Isometrizer;

pub trait EqClass: Isometrizer {
    fn is_representing(
        &self,
        term: &Term,
    ) -> bool;
}
